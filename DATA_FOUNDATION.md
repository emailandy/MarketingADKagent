# 📊 Data Foundation & Analytics Schema

This project is built on a **Unified Data Foundation** that blends internal performance metrics with official government tourism data to provide grounded, competitive market intelligence.

## 🗄️ BigQuery Datasets

All data resides in the `nodepeel.marketing_analytics` dataset.

### 1. Internal Agoda Bookings (`agoda_bookings_monthly`)
Contains country-level internal booking performance across 50+ origin markets.
| Field | Type | Description |
|-------|------|-------------|
| `Origin_Market` | STRING | The source country of the traveler. |
| `Bookings_2024` | INTEGER | Historical monthly bookings. |
| `Bookings_2025` | INTEGER | Current monthly bookings. |
| `Month` | DATE | Monthly snapshot. |

### 2. Official MOTS Arrivals (`mots_arrivals_monthly`)
Authoritative arrival data from the Ministry of Tourism and Sports (Thailand).
| Field | Type | Description |
|-------|------|-------------|
| `Country_of_Origin` | STRING | The traveler's home country. |
| `Region` | STRING | Geographic macro-region (ASEAN, EMEA, etc). |
| `Arrivals_2024` | INTEGER | Historical official arrivals. |
| `Arrivals_2025` | INTEGER | Current official arrivals. |
| `Month` | DATE | Monthly snapshot. |

### 3. OTA Performance Weekly (`ota_performance_weekly`)
Internal marketing spend and efficiency metrics.
| Field | Type | Description |
|-------|------|-------------|
| `region` | STRING | Geographic macro-region. |
| `actual_spend` | FLOAT | Total marketing spend. |
| `roas` | FLOAT | Return on Ad Spend. |
| `cac` | FLOAT | Customer Acquisition Cost. |

---

## 📈 Unified Insights Logic (`market_performance_insights`)

The core "Intelligence" layer is a BigQuery view that performs a complex join across all three foundations.

### Join Strategy
- **Primary Join**: `agoda_bookings_monthly` JOIN `mots_arrivals_monthly` 
  - **Keys**: `Origin_Market` = `Country_of_Origin` AND `Month`.
- **Enrichment**: LEFT JOIN `ota_performance_weekly`
  - **Keys**: Region-mapped normalized identifiers.

### Key Derived Metrics
1. **Penetration Rate**: `Agoda Bookings / Total MOTS Arrivals`.
2. **Market Share Velocity**: Measuring if Agoda is gaining or losing share faster than the total market recovery.
3. **Efficiency Mapping**: Correlating country-level penetration with regional `CAC` to identify underspending opportunities.

## 🤖 Agent Usage
The `DataAnalystAgent` is specifically trained to query this view as a "single source of truth" for all strategic market share questions.
