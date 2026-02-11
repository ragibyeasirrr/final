#  Hotel Booking System (Django)

A Django-based hotel booking system that allows users to browse hotels, view rooms and facilities, add rooms to a cart, and complete bookings with reviews and ratings.

---

##  Features

- Hotel categorization
- Room management with facilities and images
- User reviews and ratings
- Cart-based room booking
- Final booking with status tracking
- UUID-based secure booking IDs

---

##  Models Overview

### 1. HotelCategory
Represents different categories of hotels (e.g., Luxury, Budget).

**Fields:**
- `name` (CharField)
- `description` (TextField)

---

### 2. Hotel
Stores hotel-related information.

**Fields:**
- `name` (CharField)
- `address` (CharField)
- `description` (TextField)
- `image` (ImageField)
- `category` (ForeignKey → HotelCategory)

---

### 3. Facility
Defines facilities available in rooms.

**Fields:**
- `name` (CharField)
- `description` (TextField)

---

### 4. Room
Represents rooms inside a hotel.

**Fields:**
- `hotel` (ForeignKey → Hotel)
- `room_num` (CharField, unique)
- `cost_per_day` (DecimalField)
- `capecity` (PositiveIntegerField, 1–5)
- `facility` (ManyToMany → Facility)
- `available` (BooleanField)

---

### 5. Room Images
Stores multiple images for each room.

**Fields:**
- `rooms` (ForeignKey → Room)
- `image` (ImageField)

---

### 6. Review
Allows users to review hotels.

**Fields:**
- `hotel` (ForeignKey → Hotel)
- `user` (ForeignKey → User)
- `ratings` (PositiveIntegerField, 1–10)
- `comment` (TextField)
- `created_at` (DateTimeField)
- `updated_at` (DateTimeField)

---

### 7. Cart_Booking
Each user has one active booking cart.

**Fields:**
- `id` (UUIDField, Primary Key)
- `user` (OneToOneField → User)
- `created_at` (DateTimeField)

---

### 8. Cart_bookingRoom
Rooms added to the booking cart.

**Fields:**
- `cartbooking` (ForeignKey → Cart_Booking)
- `cartRoom` (ForeignKey → Room)

**Constraint:**
- A room can only be added once per cart (`unique_together`).

---

### 9. Booking
Stores finalized booking details.

**Fields:**
- `id` (UUIDField)
- `user` (ForeignKey → User)
- `status` (ChoiceField)
- `total_price` (DecimalField)
- `created_at` (DateTimeField)
- `updated_at` (DateTimeField)

**Booking Status Options:**
- `not paid`
- `pending`
- `booked`
- `cancel`

---

### 10. BookingRoom
Rooms included in a booking.

**Fields:**
- `booking` (ForeignKey → Booking)
- `Room` (ForeignKey → Room)
- `cost_per_day` (DecimalField)

---

##  Relationships Summary

- One **HotelCategory** → Many **Hotels**
- One **Hotel** → Many **Rooms**
- One **Room** → Many **Facilities**
- One **User** → One **Cart**
- One **Cart** → Many **Rooms**
- One **Booking** → Many **Rooms**
- One **Hotel** → Many **Reviews**

---

##  Tech Stack

- Backend: Django, Django REST Framework
- Database: SQLite / PostgreSQL
- Authentication: Custom User Model
- Media Handling: Django ImageField

---

##  Future Improvements

- Date-based room availability
- Payment gateway integration
- Admin dashboard analytics
- Discount and coupon system
- Advanced search and filtering

---

##  Author

**Ragib Yeasir**  
Aspiring Google Engineer | Django & DRF Developer
