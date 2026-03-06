from pydantic import BaseModel, EmailStr
from typing import Optional


class BookingCreate(BaseModel):
    userName: str
    userEmail: EmailStr
    userNumber: Optional[str] = None
    bookingDate: str
    bookingTime: str
    bookingAdults: int
    bookingChildren: int
    tableNumber: str


class BookingUpdate(BaseModel):
    userName: Optional[str] = None
    userEmail: Optional[EmailStr] = None
    userNumber: Optional[str] = None
    bookingDate: Optional[str] = None
    bookingTime: Optional[str] = None
    bookingAdults: Optional[int] = None
    bookingChildren: Optional[int] = None
    tableNumber: Optional[str] = None


class BookingResponse(BaseModel):
    bookingID: str
    userName: str
    userEmail: EmailStr
    userNumber: str
    bookingDate: str
    bookingTime: str
    bookingAdults: int
    bookingChildren: int
    tableNumber: str