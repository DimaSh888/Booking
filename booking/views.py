from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Booking, Room


def room_list(request):
    rooms = Room.objects.all()
    context = {
        "rooms": rooms,
    }
    return render(request, template_name="booking/room_list.html", context=context)


def book_room(request):
    if request.method == "POST":
        room_number = request.POST.get("room-number")
        start_time = request.POST.get("start-time")
        end_time = request.POST.get("end-time")

        try:
            room = Room.objects.get(number=room_number)
        except ValueError:
            return HttpResponse(
                "Wrong value for room number!",
                status=400
            )
        except Room.DoesNotExist:
            return HttpResponse(
                "This room number doesn't exist",
                status=404
            )
        booking = Booking.objects.create(
            user=request.user,
            room=room,
            start_time=start_time,
            end_time=end_time
        )
        return redirect("room-list")
    else:
        return render(request, template_name="booking/booking_form.html")
