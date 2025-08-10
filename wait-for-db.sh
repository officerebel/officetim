#!/bin/sh
set -e

host=$(echo "$1" | cut -d: -f1)
port=$(echo "$1" | cut -d: -f2)

until nc -z "$host" "$port"; do
  echo "⏳ Wachten op database ($host:$port)..."
  sleep 1
done

echo "✅ Database is klaar!"

shift  # verwijder db:5432 uit $@
exec "$@"
