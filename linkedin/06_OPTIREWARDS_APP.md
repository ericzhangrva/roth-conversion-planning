# Day 6: Building OptiRewards — The Smart Point-of-Sale Card Optimizer

*Post this on Monday morning.*
*Attach an image: A screenshot of OptiRewards recommending a card for a nearby store or showing the point valuation sliders.*

---

Part 5 of 6: Never leave money on the table at checkout.

Here is a universal consumer problem: 
Most people carry between 3 and 7 credit cards in their wallets. 

You have an Amex Gold for dining (4x), a Chase Freedom Flex for rotating 5% quarterly categories, a Citi Custom Cash for your top spend category, a US Bank Altitude Reserve for mobile wallets (4.5% net yield), and maybe a store co-branded card like Costco or Amazon.

When you are standing at the grocery counter or gas pump, you have about **two seconds** to pull out a card before the cashier looks at you awkwardly.

Almost everyone guesses. And almost everyone leaves 2% to 4% of cash back or travel points on the table.

Today, I built an app with AI to solve this exact problem: **OptiRewards**.

Here is what we engineered:

💳 **1. A Comprehensive Catalog of 168 Flagship Cards**
We built a master catalog capturing **168 distinct credit cards across 13 major banks**:
* JPMorgan Chase (45 cards)
* American Express (22 cards — personal & business)
* Capital One (35 cards)
* Bank of America (22 cards)
* Citigroup (28 cards)
* Plus Discover, Wells Fargo, U.S. Bank, Bilt, Apple Card, and more.
Every multiplier, spend limit, and rotating quarterly perk is indexed.

📍 **2. Real GPS Nearby Store Recognition**
Nobody wants to manually search a dropdown menu while standing in line.
* With one tap, OptiRewards pulls your real GPS coordinates.
* It queries physical businesses within 500 meters (grocery stores, coffee shops, gas stations, pharmacies) and shows the stores on your exact street.
* Tap the store you’re standing in, and in **under one second**, it ranks the cards in your wallet from highest to lowest effective return.

🎚️ **3. Live Point & Mile Valuation Sliders**
A point isn't always worth 1¢. 
* If you transfer Chase Ultimate Rewards to Hyatt, you might value them at **1.8¢**.
* If you redeem Amex Membership Rewards for flights, you might value them at **1.7¢**.
OptiRewards includes dynamic valuation sliders for your active cards. As you tweak your valuations, the ranking recalculates in real-time.

☁️ **4. Zero-Cost, Scalable Architecture**
Because I am a non-engineer, I didn't want a complex server infrastructure with monthly hosting bills. We designed a modern Apple-first architecture:
* **Public Catalog:** Hosted as a lightweight static JSON on a free global edge CDN (Cloudflare Pages) with unlimited bandwidth and zero server costs.
* **Private User Wallet:** Saved directly to the user's private Apple CloudKit container—meaning users never have to create an account or password, their cards sync across iPhone and Mac, and their private data never touches a third-party server.

From an everyday consumer annoyance to a working, location-aware financial utility in a single build.

Tomorrow, for the grand finale of this series: The honest, unfiltered reality. What are the real "gaps," what traps should non-engineers watch out for, and what does building with AI actually mean?

What is your current go-to credit card for everyday spending? Drop it below! 👇

#FinTech #CreditCards #PersonalFinance #ApplePay #BuildingInPublic #AIApplications #ProductDesign
