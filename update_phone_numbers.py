#!/usr/bin/env python3
import os
import re
import glob

def update_phone_numbers_in_file(file_path):
    """Update all phone numbers to the new Kenya number."""
    
    # Read the file
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    original_content = content
    
    # Define patterns to replace
    replacements = [
        # Replace old Indian phone number in various formats
        (r'\+91-9600008844', '+254711209661'),
        (r'\+91 9600008844', '+254711209661'),
        (r'919600008844', '254711209661'),
        (r'\+91 960 000 8844', '+254711209661'),
        (r'\+91-960-000-8844', '+254711209661'),
        
        # Replace any other phone number patterns that might exist
        (r'\+91[-\s]?\d{10}', '+254711209661'),
        (r'\+91[-\s]?\d{3}[-\s]?\d{3}[-\s]?\d{4}', '+254711209661'),
        
        # Update WhatsApp links
        (r'https://wa\.me/919600008844', 'https://wa.me/254711209661'),
        (r'https://web\.whatsapp\.com/send\?phone=919600008844', 'https://web.whatsapp.com/send?phone=254711209661'),
        
        # Update any other phone number references
        (r'"value":"919600008844"', '"value":"254711209661"'),
        (r'"telePhone":"\+91[^"]*"', '"telePhone":"+254711209661"'),
    ]
    
    # Apply all replacements
    for old_pattern, new_pattern in replacements:
        content = re.sub(old_pattern, new_pattern, content, flags=re.IGNORECASE)
    
    # Only write if content changed
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    return False

def main():
    """Main function to process all HTML files."""
    html_files = glob.glob('**/*.html', recursive=True)
    
    updated_count = 0
    total_files = len(html_files)
    
    print(f"Processing {total_files} HTML files...")
    
    for file_path in html_files:
        try:
            if update_phone_numbers_in_file(file_path):
                updated_count += 1
                print(f"Updated: {file_path}")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    print(f"\nSummary:")
    print(f"Total files processed: {total_files}")
    print(f"Files updated: {updated_count}")
    print(f"Success rate: {(updated_count/total_files)*100:.1f}%")

if __name__ == "__main__":
    main()

