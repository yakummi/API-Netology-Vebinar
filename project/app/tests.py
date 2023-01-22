from django.test import TestCase
import pytest

def note_factory():
    def inner():
        return baker.make('Note', make_m2m=True)

    return inner

def test_api(note_factory):
    note = note_factory(m2m=True)
    response = note.get(f"/notes/{note.id}/?is_private=true")
    data = response.json()
    assert data["id"] == note.id
    assert data["text"] == note.id