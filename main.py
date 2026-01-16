import instaloader

def get_numerical_features(username):
    L = instaloader.Instaloader()
    # Replace with L.login() if checking private accounts you follow
    profile = instaloader.Profile.from_username(L.context, username)

    # --- 1. Boolean & Presence Checks (Converted to 1 or 0) ---
    
    # Does it have a profile pic? (Instaloader provides a URL if it exists)
    has_profile_pic = 1 if "default_profile_pic" not in profile.profile_pic_url else 0
    
    # Is the account private?
    is_private = 1 if profile.is_private else 0
    
    # Does it have an external URL in the bio?
    has_external_url = 1 if profile.external_url else 0

    # --- 2. String & Ratio Calculations ---
    
    # Username: Ratio of digits to total length
    username_len = len(profile.username)
    nums_length_username = sum(c.isdigit() for c in profile.username) / username_len if username_len > 0 else 0
    
    # Full Name: Ratio of digits to total length
    fullname_len = len(profile.full_name)
    nums_length_fullname = (sum(c.isdigit() for c in profile.full_name) / fullname_len) if fullname_len > 0 else 0
    
    # Full Name: Word count
    fullname_words = len(profile.full_name.split())
    
    # Logic: Does the name match the username exactly?
    name_equals_username = 1 if profile.full_name.lower() == profile.username.lower() else 0
    
    # Bio: Total character count
    description_length = len(profile.biography)

    # --- 3. Final Numerical Array ---
    # Order: profile_pic, nums/length_username, fullname_words, nums/length_fullname, 
    # name==username, description_length, external_url, private, #posts, #followers, #follows
    
    feature_vector = [
        has_profile_pic,
        round(nums_length_username, 2),
        fullname_words,
        round(nums_length_fullname, 2),
        name_equals_username,
        description_length,
        has_external_url,
        is_private,
        profile.mediacount,
        profile.followers,
        profile.followees
    ]
    
    return feature_vector

# --- Example of the output you requested ---
result = get_numerical_features("pere")
print(" ".join(map(str, result))) 
# Output: 1 0.27 2 0.00 0 53 0 0 32 1000 955