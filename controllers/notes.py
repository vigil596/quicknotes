from flask import Blueprint, jsonify, request

notes_bp = Blueprint("notes", __name__)

_notes = []


@notes_bp.get("/notes")
def list_notes():
    return jsonify(_notes)


@notes_bp.post("/notes")
def create_note():
    data = request.get_json(silent=True) or {}
    note = {"id": len(_notes) + 1, "text": data.get("text", "")}
    _notes.append(note)
    return jsonify(note), 201
