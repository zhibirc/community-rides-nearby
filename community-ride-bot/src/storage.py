"""
Storage interface for Community Rides.
"""

from typing import List, Optional, TypedDict, Literal

# Mongo ObjectId string, can be int/uuid in other backends.
RideId = str

# Optional lifecycle statuses.
RideStatus = Literal["active", "cancelled", "expired"]

class Ride(TypedDict, total=False):
    id: str
    user_id: int
    from_location: str
    to_location: str
    capacity: int
    time_range: str
    comment: str
    created_at: str
    status: RideStatus

def create_ride(
    user_id: int,
    from_location: str,
    to_location: str,
    capacity: int,
    time_range: Optional[str] = None,
    comment: Optional[str] = None
) -> RideId:
    """
    Insert a new ride and return its identifier.

    Args (schema can be extended):
        user_id: Telegram user ID of the ride owner/creator.
        from_location: Human-readable start location (free text or later geo).
        to_location: Human-readable destination (free text or later geo).
        capacity: Number of free seats; must be >= 1.
        time_range: Optional free-text time window (e.g., "2025-11-06 15:00-17:00").
        comment: Optional free-text note for passengers, e.g. "There is a child seat."

    Returns:
        A ride identifier (string for Mongo ObjectId, or other type cast to str).

    Raises:
        ValueError: If required fields are empty or capacity < 1.
        RuntimeError: On storage/connection errors.
    """
    pass


def update_ride(user_id: int, ride_id: RideId, patch: Ride) -> bool:
    """
    Update an existing ride.

    Expected behavior:
        - Only allow updates to fields such as from_location, to_location, capacity, time_range, comment, status.
        - Validate values (e.g., capacity >= 1).
        - Return True if updated, False if not found or not owned.

    Raises:
        ValueError: On invalid update values.
        RuntimeError: On storage failures.
    """
    pass


def fetch_rides(user_id: int, active_only: bool) -> List[Ride]:
    """
    Fetch rides for a given user, with an option to filter active ones.

    Consider adding pagination.

    Args:
        user_id: Telegram user ID. Only rides created by this user are returned.
        active_only: If True, return only non-cancelled/non-expired rides.

    Returns:
        Iterable (e.g., list) of ride dicts. Each dict should at minimum include:
        {
            "id": <ride id (int or str)>,
            "user_id": int,
            "from_location": str,
            "to_location": str,
            "capacity": int,
            "time_range": str,
            "comment": str,
            "created_at": <datetime/ISO-string>,
            "status": "active" | "cancelled" | "expired"  (if implemented)
        }

    Raises:
        RuntimeError: On storage/connection errors.
    """
    pass


def delete_ride(user_id: int, ride_id: RideId, deactivate_only: bool) -> bool:
    """
    Remove or deactivate a ride.

    If "deactivate_only" is True, perform a soft delete (e.g., status="cancelled").
    Otherwise perform a hard delete.

    Args:
        user_id: Owner's Telegram user ID.
        ride_id: Identifier of the ride to delete.
        deactivate_only: True for soft delete, False for hard delete.

    Returns:
        True if a ride was affected; False if not found or not owned.

    Raises:
        RuntimeError: On storage/connection errors.
    """
    pass
