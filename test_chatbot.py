import pytest
from chatbot import respond

def test_known_input():
    input_text = "hello"
    response = respond(input_text)
    assert isinstance(response, str)
    assert response != "Sorry, I don't understand that. Try asking something else."

def test_unknown_input():
    input_text = "what is the capital of Mars?"
    response = respond(input_text)
    assert response == "Sorry, I don't understand that. Try asking something else."
