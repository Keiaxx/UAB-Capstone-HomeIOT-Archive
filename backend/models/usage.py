# Contributor(s): Adrian Gose
# If you worked on this file, add your name above so we can keep track of contributions

from extensions.database import db


class Usage(db.Model):
    __tablename__ = "usage"
    usageId = db.Column(db.Integer, primary_key=True)
    deviceId = db.Column(db.Integer, db.ForeignKey("device.deviceId"))
    date = db.Column(db.DATETIME, nullable=False)
    type = db.Column(db.Enum('water', 'electric'), nullable=False)
    data = db.Column(db.Integer)

    device = db.relationship("Device", back_populates="usages")

    def __repr__(self):
        return f'<Usage | Type: {self.type}>'

    def __init__(self, device, date, type, data):
        self.device = device
        self.date = date
        self.type = type
        self.data = data