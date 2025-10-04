from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from item.models import Item
from .forms import ConversationMessageForm
from .models import Conversation, ConversationMessage


@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    # Prevent messaging yourself
    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    # Check if a conversation already exists between the user and the item
    conversation = Conversation.objects.filter(item=item, members=request.user).first()
    if conversation:
        return redirect('conversation:detail', pk=conversation.id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            # Create a new conversation
            conversation = Conversation.objects.create(item=item)
            # Ensure both the requester and the item owner are members
            conversation.members.add(request.user, item.created_by)

            # Save the first message
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail', pk=item_pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/new.html', {
        'form': form,
        'item': item
    })


@login_required
def inbox(request):
    # Get all conversations where the current user is a member
    conversations = Conversation.objects.filter(members=request.user).distinct()

    return render(request, 'conversation/inbox.html', {
        'conversations': conversations
    })


@login_required
def detail(request, pk):
    # Ensure user is a member of the conversation
    conversation = get_object_or_404(Conversation, pk=pk, members=request.user)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            return redirect('conversation:detail', pk=pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/detail.html', {
        'conversation': conversation,
        'form': form
    })
