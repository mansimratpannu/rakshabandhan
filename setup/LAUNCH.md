# 🚀 Launch Checklist: Raksha Bandhan 2026 Storefront

Follow these steps to import your products, configure metafields, hook up the theme customizer, and successfully go live.

---

## 1. Import Product Catalog
1. Go to **Shopify Admin** > **Products**.
2. Click **Import** in the top-right corner.
3. Upload the [products.csv](file:///c:/Users/mansi/OneDrive/Desktop/Projects%20for%20fun/rakshabandhan/setup/products.csv) file.
4. Check the box "Publish new products to all sales channels" and click **Upload and continue**.
5. Once imported, verify that the **Traditional Roli-Chawal Packet** is active and priced at **0.00**.

---

## 2. Set Up Metafields (Custom Data)
To enable variant lines and facets:
1. Go to **Shopify Admin** > **Settings** > **Custom data**.
2. Click **Products** > **Add definition**.
3. Create the following three metafield definitions exactly as specified:
   - **Name**: `Material` | **Namespace & key**: `custom.material` | **Type**: `Single line text`.
   - **Name**: `Set Size` | **Namespace & key**: `custom.set_size` | **Type**: `Integer`.
   - **Name**: `Occasion` | **Namespace & key**: `custom.occasion` | **Type**: `Single line text`.
4. Fill in these metafield fields on individual product pages inside your Shopify Admin to populate details.

---

## 3. Enable Native Collection Filters
1. Go to **Shopify Admin** > **Online Store** > **Navigation**.
2. Under **Collection filters**, click **Add Filters**.
3. Choose **Price**, **Product Type**, and the custom metafields: **Material**, **Set Size**, and **Occasion**.
4. Click **Save**.

---

## 4. Hook Up the Theme in Shopify Admin
1. Go to **Shopify Admin** > **Online Store** > **Themes**.
2. Click **Add Theme** > **Connect from GitHub**.
3. Connect your repository: `https://github.com/mansimratpannu/rakshabandhan.git` (branch: `main`).
4. Once connected, click **Customize** to open the visual editor.

---

## 5. Visual Customizer Adjustments
1. **Festive Hero Section**:
   - Upload your high-res hero image in the customizer.
   - Adjust the **Countdown Date** to your final order cutoff (e.g. `2026-08-25T23:59:59`).
2. **Collection Tiles**:
   - Assign the custom collections to each of the 5 category tiles.
3. **Cart settings**:
   - Go to **Theme Settings** > **Cart**.
   - Make sure cart type is set to **Drawer**.
   - Verify the **Free Shipping Threshold** setting or let it default to ₹1000.

---

## 6. Pre-Launch Verification Checks
- [ ] **Desktop Buy Box**: Open a product page and check that the buy box is sticky while scrolling media.
- [ ] **Color Swatches**: Verify that colors (e.g. "Kumkum Red") render swatches dynamically.
- [ ] **Gift Message**: Type a message on the product page, add to cart, and check that the property `Gift Message` is stored in the cart object.
- [ ] **Pincode Delivery Estimator**: Type `110001` (Delhi) and check that it estimates arrival within 2 days. Type a pincode causing a late arrival to confirm the Kumkum red cutoff warnings show up.
- [ ] **Free Roli-Chawal Toggle**: Open the cart drawer, check the toggle to confirm the free item is added, and uncheck it to confirm it gets removed.
- [ ] **Mobile Responsive check**: Check announcement countdown, sticky mobile bar, collection tiles, and hamper builder on mobile screen simulations.
