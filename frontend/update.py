#!/usr/bin/env python3
"""
Revert links back to .html for local testing
Run this when testing locally, then run update_links.py before deploying
"""

import os
from pathlib import Path

# Reverse mappings: clean URLs → .html
REVERT_MAPPINGS = {
    # Homepage
    'href="/"': 'href="index.html"',
    "href='/'": "href='index.html'",
    
    # Main pages
    'href="/main"': 'href="main.html"',
    'href="/flights"': 'href="flights.html"',
    'href="/trains"': 'href="trains.html"',
    'href="/buses"': 'href="buses.html"',
    'href="/cabs"': 'href="cabs.html"',
    'href="/hotels"': 'href="hotels.html"',
    'href="/tours"': 'href="tours.html"',
    'href="/cruise"': 'href="cruise.html"',
    'href="/insurance"': 'href="insurance.html"',
    
    # User pages
    'href="/login"': 'href="login.html"',
    'href="/signup"': 'href="signup.html"',
    'href="/profile"': 'href="profile.html"',
    'href="/upcoming"': 'href="upcoming.html"',
    'href="/completed"': 'href="completed.html"',
    'href="/wallent"': 'href="wallent.html"',
    'href="/plan"': 'href="plan.html"',
    'href="/discover"': 'href="discover.html"',
    'href="/ticket"': 'href="ticket.html"',
    
    # JavaScript window.location.href
    'window.location.href = "/main"': 'window.location.href = "main.html"',
    'window.location.href = "/login"': 'window.location.href = "login.html"',
    'window.location.href = "/signup"': 'window.location.href = "signup.html"',
    'window.location.href = "/"': 'window.location.href = "index.html"',
    'window.location.href = "/flights"': 'window.location.href = "flights.html"',
    'window.location.href = "/trains"': 'window.location.href = "trains.html"',
    'window.location.href = "/buses"': 'window.location.href = "buses.html"',
    'window.location.href = "/cabs"': 'window.location.href = "cabs.html"',
    'window.location.href = "/hotels"': 'window.location.href = "hotels.html"',
    'window.location.href = "/tours"': 'window.location.href = "tours.html"',
    
    # Single quotes
    "window.location.href = '/main'": "window.location.href = 'main.html'",
    "window.location.href = '/login'": "window.location.href = 'login.html'",
    "window.location.href = '/signup'": "window.location.href = 'signup.html'",
    
    # Query strings
    '`/ticket?id=': '`ticket.html?id=',
    '`/plan?destination=': '`plan.html?destination=',
    '`/plan?search=': '`plan.html?search=',
}

def revert_file(file_path):
    """Revert navigation links in a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        replacements_made = []
        
        for clean_url, html_link in REVERT_MAPPINGS.items():
            if clean_url in content:
                content = content.replace(clean_url, html_link)
                replacements_made.append(clean_url)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, len(replacements_made)
        
        return False, 0
        
    except Exception as e:
        print(f"  ❌ Error processing {file_path.name}: {e}")
        return False, 0

def main():
    print("🔙 Reverting Links for Local Development")
    print("=" * 60)
    print()
    
    current_dir = Path(".")
    html_files = list(current_dir.glob("*.html"))
    js_files = list(current_dir.glob("*.js"))
    
    if not html_files:
        print("❌ Error: No HTML files found!")
        return
    
    print(f"📁 Found {len(html_files)} HTML files and {len(js_files)} JS files")
    print()
    
    # Process HTML files
    print("📄 Reverting HTML files...")
    updated_html = 0
    
    for file_path in sorted(html_files):
        changed, count = revert_file(file_path)
        if changed:
            print(f"  ✅ Reverted: {file_path.name} ({count} replacements)")
            updated_html += 1
        else:
            print(f"  ⚪ No changes: {file_path.name}")
    
    # Process JavaScript files
    print()
    print("📜 Reverting JavaScript files...")
    updated_js = 0
    
    for file_path in sorted(js_files):
        changed, count = revert_file(file_path)
        if changed:
            print(f"  ✅ Reverted: {file_path.name} ({count} replacements)")
            updated_js += 1
        else:
            print(f"  ⚪ No changes: {file_path.name}")
    
    print()
    print("=" * 60)
    print("✅ Links reverted to .html for local testing!")
    print(f"   📊 Updated {updated_html} HTML file(s) and {updated_js} JS file(s)")
    print()
    print("💡 Now you can:")
    print("   • Open index.html directly in browser")
    print("   • Use Live Server")
    print("   • Test locally without issues")
    print()
    print("⚠️  Before deploying to Vercel:")
    print("   Run: python update_links.py")

if __name__ == "__main__":
    main()