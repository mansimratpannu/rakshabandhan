# Shopify Metafields Configuration Mapping

To enable all advanced filtering and layout options in the theme customizer, configure the following metafields inside your Shopify Admin:

## 1. Product Metafields

| Namespace & Key | Content Type | Label / Name | Description | Used For |
| :--- | :--- | :--- | :--- | :--- |
| `custom.material` | Single line text | Material | Material component of the Rakhi (e.g., Sandalwood, Silk thread, Brass) | Displayed on product cards and filters |
| `custom.set_size` | Integer | Set Size | Number of rakhis included in the purchase (e.g., 1, 2, 4) | Product variant info line and filtering |
| `custom.occasion` | Single line text | Occasion | Occasion tags (e.g. Sibling Gifting, Bhaiya-Bhabhi ceremony) | Collection grid filtering |

---

## 2. Storefront Navigation Filters Configuration

To activate these filters on the Collection grid without any external apps:
1. Go to **Shopify Admin** > **Online Store** > **Navigation**.
2. Scroll down to **Collection filters** section.
3. Click **Add Filters**.
4. Check the following native filters:
   - **Product Type** (e.g., Classic Rakhi, Bhaiya-Bhabhi Set, Pooja Thali, Hampers)
   - **Price**
   - **Availability**
5. Check the custom product metafield filters:
   - **Material** (`custom.material`)
   - **Set Size** (`custom.set_size`)
   - **Occasion** (`custom.occasion`)
6. Click **Save**.

---

## 3. Creating the Free Roli-Chawal Packet Product

To ensure the free packet checkbox works in the cart drawer:
1. Go to **Shopify Admin** > **Products** > **Add Product**.
2. Set the Title to: `Traditional Roli-Chawal Packet`
3. Set the Handle to: `roli-chawal-packet`
4. Set the Price to: `0.00`
5. Set the Compare At Price to: `0.00`
6. Add the Tag: `RoliChawal`
7. Set the Product Status to: **Active**
8. Set the Inventory policy to **Continue selling when out of stock**.
9. Click **Save**.
