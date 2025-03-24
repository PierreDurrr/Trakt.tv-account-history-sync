# Trakt.tv-account-history-sync
Sync trakt.tv viewing history acrosse 2 account (doesn't preserve viewing date for now)
---

Here's a **basic Python script** to sync watched history from one Trakt account to another using the **Trakt API**. This script:  

✅ Logs into **Account 1**  
✅ Fetches watched history (movies & episodes)  
✅ Logs into **Account 2**  
✅ Adds the history to **Account 2**  

---

### **🔧 Steps to Use the Script**  
1. Get a **Trakt API key**:  
   - Go to [Trakt API Settings](https://trakt.tv/oauth/applications)  
   - Create a new app  
   - Get your **Client ID** & **Client Secret**  

2. Replace the placeholders in the script with your credentials.  

3. Run the script in **Python 3**.  

---

### **💡 How It Works**
1. **Authenticates both accounts manually** using Trakt's OAuth.  
2. **Fetches the watched history** from Account 1.  
3. **Adds it to Account 2** so both accounts stay in sync.  

### **✅ Features**
- Works for both **movies & episodes**  
- **No API limits** (since Trakt allows syncing freely)  
- **Minimal setup** (no extra libraries needed)  

---

### **📌 Notes**
- This **DOESN'T** preserve viewing date. Everything will be added at the date which the script is running.
- This **only syncs watched history**. If you need **ratings, watchlists, or collections**, the API endpoints can be modified.  
- You must **authenticate manually** for each account (Trakt doesn't allow full automation for non-VIP users).  
