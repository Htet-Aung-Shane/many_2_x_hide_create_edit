# Web Hide Many2 X Option

## Overview

The **Web Hide Many2 X Option** module customizes Odoo’s web client by **removing the "Create" and "Edit" options** from `Many2One` and `Many2Many` fields.
This helps enforce stricter data integrity and ensures that users can only select from existing records instead of creating or editing them directly from form views.

---

## Features

* 🚫 Hides the **"Create"** option in `Many2One` and `Many2Many` fields.
* 🚫 Hides the **"Edit"** option in `Many2One` and `Many2Many` fields.
* 🔒 Ensures better data consistency by restricting direct modifications.
* 🖥️ Lightweight web customization, compatible with Odoo **18.0**.

---

## Technical Details

* **Module Name:** `web_hide_many_2_x`
* **Version:** 18.0.0.0
* **License:** LGPL-3
* **Dependencies:** `web`

This module injects custom JavaScript into the **backend assets**:

* `static/src/js/many_2_one.js` → Handles `Many2One` fields.
* `static/src/js/many_2_many.js` → Handles `Many2Many` fields.

---

## Installation

1. Download or clone this module into your Odoo `addons` directory:

   ```bash
   git clone https://github.com/mttech-mm/web_hide_many_2_x.git
   ```
2. Restart your Odoo server.
3. Activate **Developer Mode** in Odoo.
4. Navigate to **Apps > Update Apps List**.
5. Search for **Web Hide Many2 X Option** and install it.

---

## Usage

Once installed, the module works automatically:

* Open any form view with `Many2One` or `Many2Many` fields.
* The **"Create"** and **"Edit"** options will be hidden from the dropdown menu.

No extra configuration is required. ✅

---

## Author

* **MT Tech**
* 🌐 [https://mttech-mm.com](https://mttech-mm.com)

---

Do you want me to also add **screenshots (placeholders)** in the README so users can visually see the "before and after" effect in the dropdowns?

## Screenshots

### Before installing
![Before](screenshot_before.png)

### After installing
![After](screenshot_after.png)
