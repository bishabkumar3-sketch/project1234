"""
SVG module for android pattern cracker
Generates SVG representations of gesture patterns
"""

def draw(pattern):
    """
    Draw a gesture pattern as an SVG.
    
    Args:
        pattern: A string of digits (0-8) representing pattern coordinates
        
    Returns:
        SVG string representation of the pattern
    """
    
    # Grid layout for 3x3 Android pattern lock
    # Positions: 0 1 2
    #           3 4 5
    #           6 7 8
    
    grid_positions = {
        '0': (50, 50),
        '1': (150, 50),
        '2': (250, 50),
        '3': (50, 150),
        '4': (150, 150),
        '5': (250, 150),
        '6': (50, 250),
        '7': (150, 250),
        '8': (250, 250),
    }
    
    # Start SVG document
    svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="300" height="300" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="300" height="300" fill="white" stroke="black" stroke-width="2"/>
  
  <!-- Grid dots -->'''
    
    # Add grid circles
    for pos, (x, y) in grid_positions.items():
        svg += f'\n  <circle cx="{x}" cy="{y}" r="15" fill="lightgray" stroke="black" stroke-width="1"/>'
    
    # Draw pattern lines
    if pattern:
        points = []
        for digit in pattern:
            if digit in grid_positions:
                points.append(grid_positions[digit])
        
        if points:
            # Draw connecting lines
            for i in range(len(points) - 1):
                x1, y1 = points[i]
                x2, y2 = points[i + 1]
                svg += f'\n  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="blue" stroke-width="3"/>'
            
            # Highlight pattern points
            for i, (x, y) in enumerate(points):
                color = "red" if i == 0 else "orange"
                svg += f'\n  <circle cx="{x}" cy="{y}" r="12" fill="{color}" stroke="darkred" stroke-width="2"/>'
                svg += f'\n  <text x="{x}" y="{y + 5}" text-anchor="middle" font-size="12" fill="white">{i + 1}</text>'
    
    svg += '\n</svg>'
    return svg
