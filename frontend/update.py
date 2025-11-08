#!/usr/bin/env python3
"""
Update all navigation links in HTML and JS files for Vercel deployment
Removes .html extensions and uses clean URLs
"""

import os
import re
from pathlib import Path

# Link mapping: old → new
LINK_MAPPINGS = {
    # Homepage
    'href="getstart.html"': 'href="/"',
    'href="index.html"': 'href="/"',
    "href='getstart.html'": "href='/'",
    "href='index.html'": "href='/'",
    
    # Main navigation pages
    'href="main.html"': 'href="/main"',
    'href="flights.html"': 'href="/flights"',
    'href="trains.html"': 'href="/trains"',
    'href="buses.html"': 'href="/buses"',
    'href="cabs.html"': 'href="/cabs"',
    'href="hotels.html"': 'href="/hotels"',
    'href="tours.html"': 'href="/tours"',
    'href="cruise.html"': 'href="/cruise"',
    'href="insurance.html"': 'href="/insurance"',
    
    # User pages
    'href="login.html"': 'href="/login"',
    'href="signup.html"': 'href="/signup"',
    'href="profile.html"': 'href="/profile"',
    'href="upcoming.html"': 'href="/upcoming"',
    'href="completed.html"': 'href="/completed"',
    'href="wallent.html"': 'href="/wallent"',
    'href="plan.html"': 'href="/plan"',
    'href="discover.html"': 'href="/discover"',
    'href="ticket.html"': 'href="/ticket"',
    
    # JavaScript window.location.href
    'window.location.href = "main.html"': 'window.location.href = "/main"',
    'window.location.href = "login.html"': 'window.location.href = "/login"',
    'window.location.href = "signup.html"': 'window.location.href = "/signup"',
    'window.location.href = "profile.html"': 'window.location.href = "/profile"',
    'window.location.href = "getstart.html"': 'window.location.href = "/"',
    'window.location.href = "index.html"': 'window.location.href = "/"',
    'window.location.href = "flights.html"': 'window.location.href = "/flights"',
    'window.location.href = "trains.html"': 'window.location.href = "/trains"',
    'window.location.href = "buses.html"': 'window.location.href = "/buses"',
    'window.location.href = "cabs.html"': 'window.location.href = "/cabs"',
    'window.location.href = "hotels.html"': 'window.location.href = "/hotels"',
    'window.location.href = "tours.html"': 'window.location.href = "/tours"',
    'window.location.href = "cruise.html"': 'window.location.href = "/cruise"',
    'window.location.href = "insurance.html"': 'window.location.href = "/insurance"',
    'window.location.href = "upcoming.html"': 'window.location.href = "/upcoming"',
    'window.location.href = "completed.html"': 'window.location.href = "/completed"',
    'window.location.href = "wallent.html"': 'window.location.href = "/wallent"',
    
    # Single quotes variant
    "window.location.href = 'main.html'": "window.location.href = '/main'",
    "window.location.href = 'login.html'": "window.location.href = '/login'",
    "window.location.href = 'signup.html'": "window.location.href = '/signup'",
    "window.location.href = 'getstart.html'": "window.location.href = '/'",
}

def update_file(file_path):
    """Update navigation links in a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        replacements = 0
        
        # Apply all mappings
        for old_link, new_link in LINK_MAPPINGS.items():
            if old_link in content:
                content = content.replace(old_link, new_link)
                replacements += 1
        
        # Only write if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, replacements
        
        return False, 0
        
    except Exception as e:
        print(f"  ❌ Error processing {file_path.name}: {e}")
        return False, 0

def main():
    print("🔗 Updating Navigation Links for Vercel Deployment")
    print("=" * 50)
    print()
    
    # Find the frontend directory
    frontend_dir = Path("travel-mate/frontend")
    
    if not frontend_dir.exists():
        # Try current directory
        frontend_dir = Path("frontend")
        if not frontend_dir.exists():
            # Try looking in current directory for HTML files
            frontend_dir = Path(".")
            html_files = list(frontend_dir.glob("*.html"))
            if not html_files:
                print("❌ Error: Could not find HTML files!")
                print("   Please run this script from the project root or frontend directory.")
                return
    
    # Process HTML files
    print("📄 Processing HTML files...")
    html_files = list(frontend_dir.glob("*.html"))
    updated_html = 0
    
    for file_path in html_files:
        changed, count = update_file(file_path)
        if changed:
            print(f"  ✓ Updated: {file_path.name} ({count} replacements)")
            updated_html += 1
    
    if updated_html == 0:
        print("  ℹ️  No HTML files needed updating")
    
    # Process JavaScript files
    print()
    print("📜 Processing JavaScript files...")
    js_files = list(frontend_dir.glob("*.js"))
    updated_js = 0
    
    for file_path in js_files:
        changed, count = update_file(file_path)
        if changed:
            print(f"  ✓ Updated: {file_path.name} ({count} replacements)")
            updated_js += 1
    
    if updated_js == 0:
        print("  ℹ️  No JavaScript files needed updating")
    
    # Summary
    print()
    print("✅ Link update complete!")
    print(f"   Updated {updated_html} HTML file(s) and {updated_js} JS file(s)")
    print()
    print("📋 Changes made:")
    print("   • .html extensions removed from all navigation links")
    print("   • Clean URLs: /main, /flights, /login, etc.")
    print("   • Homepage links updated to /")
    print()
    print("🎉 Your files are now ready for Vercel deployment!")
    print()
    print("Next steps:")
    print("  1. cd travel-mate")
    print("  2. vercel (or push to GitHub for auto-deploy)")

if __name__ == "__main__":
    main()