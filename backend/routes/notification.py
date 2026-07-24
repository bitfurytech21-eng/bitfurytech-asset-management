from flask import Blueprint, jsonify
from models.notification import Notification

notification_bp = Blueprint("notification", __name__)


@notification_bp.route("/notifications", methods=["GET"])
def get_notifications():

    notifications = Notification.query.order_by(
        Notification.created_at.desc()
    ).all()

    return jsonify({
        "success": True,
        "count": len(notifications),
        "notifications": [
            notification.to_dict()
            for notification in notifications
        ]
    })


@notification_bp.route("/notification/<int:notification_id>", methods=["GET"])
def get_notification(notification_id):

    notification = Notification.query.get(notification_id)

    if not notification:
        return jsonify({
            "success": False,
            "message": "Notification not found."
        }), 404

    return jsonify({
        "success": True,
        "notification": notification.to_dict()
    })
