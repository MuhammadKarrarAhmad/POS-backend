from fastapi import APIRouter, HTTPException
import uuid

from POS.models import BookingCreate, BookingUpdate, BookingResponse

POS_router = APIRouter()

bookings = []


@POS_router.post("/bookings", response_model=BookingResponse)
def create_booking(data: BookingCreate):
    booking_id = str(uuid.uuid4())

    new_booking = {
        "bookingID": booking_id,
        "userName": data.userName,
        "userEmail": data.userEmail,
        "userNumber": data.userNumber,
        "bookingDate": data.bookingDate,
        "bookingTime": data.bookingTime,
        "bookingAdults": data.bookingAdults,
        "bookingChildren": data.bookingChildren,
        "tableNumber": data.tableNumber
    }

    bookings[booking_id] = new_booking
    return new_booking


@POS_router.get("/bookings", response_model=list[BookingResponse])
def get_all_bookings():
    return list(bookings.values())


@POS_router.get("/bookings/{booking_id}", response_model=BookingResponse)
def get_booking(booking_id: str):
    booking = bookings.get(booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking


@POS_router.put("/bookings/{booking_id}", response_model=BookingResponse)
def update_booking(booking_id: str, data: BookingUpdate):
    booking = bookings.get(booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    if data.userName is not None:
        booking["userName"] = data.userName
    if data.userEmail is not None:
        booking["userEmail"] = data.userEmail
    if data.userNumber is not None:
        booking["userNumber"] = data.userNumber
    if data.bookingDate is not None:
        booking["bookingDate"] = data.bookingDate
    if data.bookingTime is not None:
        booking["bookingTime"] = data.bookingTime
    if data.bookingAdults is not None:
        booking["bookingAdults"] = data.bookingAdults
    if data.bookingChildren is not None:
        booking["bookingChildren"] = data.bookingChildren
    if data.tableNumber is not None:
        booking["tableNumber"] = data.tableNumber

    bookings[booking_id] = booking
    return booking


@POS_router.delete("/bookings/{booking_id}")
def delete_booking(booking_id: str):
    if booking_id not in bookings:
        raise HTTPException(status_code=404, detail="Booking not found")

    del bookings[booking_id]
    return {"message": "Booking deleted successfully"}