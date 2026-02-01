#!/bin/bash

# This script is called to verify system security
# It executes /readflag and solves the mathematical challenge

# Execute /readflag and capture its output
OUTPUT=$(/readflag 2>&1)

# Extract the mathematical expression (format: ((((a op b) op c) op d) op e))
EXPR=$(echo "$OUTPUT" | grep -oP '\(\(\(\([0-9]+[+\-\*/][0-9]+\)[+\-\*/][0-9]+\)[+\-\*/][0-9]+\)[+\-\*/][0-9]+\)')

if [ -z "$EXPR" ]; then
    # Try a simpler pattern
    EXPR=$(echo "$OUTPUT" | grep -oP '\(\(\(\(.*?\)\)\)\)')
fi

if [ -z "$EXPR" ]; then
    echo "Error: Could not find mathematical expression in /readflag output." >&2
    echo "Output was: $OUTPUT" >&2
    # Still try to run /readflag interactively
    exit 1
fi

# Calculate the result using Python
RESULT=$(python3 -c "print(eval('$EXPR'))" 2>/dev/null)

if [ -z "$RESULT" ]; then
    echo "Error: Could not calculate result for expression: $EXPR" >&2
    exit 1
fi

# Send the result back to /readflag's stdin and capture the final output
echo "$RESULT" | /readflag
