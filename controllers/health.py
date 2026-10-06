from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)


@health_bp.get("/health")
def status():
    return jsonify(app="quicknotes", status="ok")
