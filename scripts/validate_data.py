#!/usr/bin/env python3
"""
Data Validation Script
Validates JSON files against their schemas
"""

import json
import sys
from pathlib import Path
from jsonschema import validate, ValidationError, Draft7Validator

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def validate_file(data_file, schema_file):
    """Validate data file against schema"""
    try:
        data = load_json(data_file)
        schema = load_json(schema_file)

        # Validate
        validator = Draft7Validator(schema)
        errors = list(validator.iter_errors(data))

        if errors:
            print(f"❌ Validation failed for {data_file.name}")
            for error in errors:
                print(f"  - {error.message}")
                print(f"    Path: {' -> '.join(str(p) for p in error.path)}")
            return False
        else:
            print(f"✅ {data_file.name} is valid")
            return True

    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in {data_file.name}: {e}")
        return False
    except Exception as e:
        print(f"❌ Error validating {data_file.name}: {e}")
        return False

def main():
    """Main validation function"""
    base_dir = Path(__file__).parent.parent
    data_dir = base_dir / 'data'
    schema_dir = data_dir / 'schemas'

    # Define validation pairs
    validations = [
        ('sources_raw.json', 'sources_raw.schema.json'),
        ('sources_with_engagement.json', 'sources_with_engagement.schema.json'),
        ('scored_sources.json', 'scored_sources.schema.json'),
        ('selected_topics.json', 'selected_topics.schema.json'),
    ]

    print("🔍 Validating data files...\n")

    all_valid = True
    for data_file, schema_file in validations:
        data_path = data_dir / data_file
        schema_path = schema_dir / schema_file

        if not data_path.exists():
            print(f"⚠️  {data_file} not found, skipping")
            continue

        if not schema_path.exists():
            print(f"❌ Schema {schema_file} not found")
            all_valid = False
            continue

        if not validate_file(data_path, schema_path):
            all_valid = False

    print()
    if all_valid:
        print("✅ All validations passed!")
        return 0
    else:
        print("❌ Some validations failed")
        return 1

if __name__ == '__main__':
    sys.exit(main())
