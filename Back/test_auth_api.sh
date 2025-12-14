#!/bin/bash
# Test script pour API Django

BASE_URL="http://127.0.0.1:8000/api/accounts"

echo "=== Test 1: Signup ==="
curl -s -X POST "$BASE_URL/signup/" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@isoc.local",
    "username": "testuser",
    "password": "testpass123456",
    "password_confirm": "testpass123456",
    "first_name": "Test",
    "last_name": "User"
  }' | python -m json.tool

echo -e "\n\n=== Test 2: Login ==="
curl -s -X POST "$BASE_URL/login/" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@isoc.local",
    "password": "testpass123456",
    "remember_me": true
  }' | python -m json.tool

echo -e "\n\n=== Test 3: Password Reset ==="
curl -s -X POST "$BASE_URL/password_reset/" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@isoc.local"
  }' | python -m json.tool

echo -e "\n\nTests completed!"
