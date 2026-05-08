import json
import os

# Paths
data_path = '/home/revenant/visual-architect/data.json'
full_data_path = '/home/revenant/visual-architect/PROJECT_DATA_FULL.json'

with open(data_path, 'r') as f:
    data = json.load(f)

with open(full_data_path, 'r') as f:
    full_data = json.load(f)

# Create a mapping from title/path to full metadata
full_map = {}
for item in full_data:
    # Normalize title for matching
    title = item['title'].lower().strip()
    full_map[title] = item
    
    # Also map by filename without extension
    filename_no_ext = os.path.splitext(os.path.basename(item['path']))[0].lower()
    full_map[filename_no_ext] = item

# Update data.json categories
for category in data.get('categories', []):
    for file_item in category.get('files', []):
        name = file_item['name'].lower().strip()
        filename_no_ext = os.path.splitext(os.path.basename(file_item['mediaUrl']))[0].lower()
        
        match = full_map.get(name) or full_map.get(filename_no_ext)
        
        if match:
            # Update path to use the new .mp4 if it was .m4v
            if file_item['mediaUrl'].endswith('.m4v'):
                file_item['mediaUrl'] = file_item['mediaUrl'].replace('.m4v', '.mp4')
            
            # Update technical info
            file_item['technical'] = {
                'resolution': match['technical_specs']['resolution'],
                'fps': str(match['technical_specs']['fps']),
                'duration': match['duration']
            }
            # Update description if it's generic
            if 'description' not in file_item or 'experimental' in file_item['description'].lower():
                file_item['description'] = match['summary']
            
            # Add tags if present
            if 'style_tags' in match:
                file_item['tags'] = match['style_tags']

# Update YouTube projects if possible (though PROJECT_DATA_FULL seems to be local files)

with open(data_path, 'w') as f:
    json.dump(data, f, indent=2)

print("data.json updated successfully.")
