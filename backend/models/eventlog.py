# Contributor(s): Adrian Gose
# If you worked on this file, add your name above so we can keep track of contributions

from extensions.database import db


class EventLog(db.Model):
    __tablename__ = "eventlog"
    eventId = db.Column(db.Integer, primary_key=True)
    deviceId = db.Column(db.Integer, db.ForeignKey("device.deviceId"))
    date = db.Column(db.DATETIME, nullable=False)
    state = db.Column(db.Enum('ON', 'OFF', 'OFFLINE', 'ERROR'), default='OFF', nullable=False)

    device = db.relationship("Device", back_populates="events")

    def __repr__(self):
        return f'<EventLog | DeviceId: {self.deviceId}>'

    def __init__(self, device, state, date):
        self.device = device
        self.state = state
        self.date = date