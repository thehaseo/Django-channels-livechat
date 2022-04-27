from django.shortcuts import redirect, render


def home(request):

    if request.method == 'POST':
        room_name = request.POST.get('room_name')
        username = request.POST.get('username')
        return redirect(f'/chat/{room_name}/?username={username}')
    return render(request, 'chat/home.html')


def room(request, room_name):
    user = request.GET.get('username')
    context = {
        'room_name': room_name,
        'user': user
    }
    return render(request, 'chat/chatroom.html', context)