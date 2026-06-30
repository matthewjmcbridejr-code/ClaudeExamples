# LifeOS E-Paper Display Plan

## Purpose

The e-paper display should act as a quiet household dashboard, not a noisy tablet.

It should show the highest-value information for the current day.

## First display content

- date
- today's top household tasks
- assigned owner for each task
- task status
- next few calendar items
- simple notes or household reminders

## Refresh cadence

Recommended starting point:

- refresh every 15 to 30 minutes during active hours
- refresh less often overnight
- manual refresh option later

## Data source

The app should eventually expose a display-safe endpoint such as:

```text
GET /api/display/today
```

The endpoint should return only information approved for shared household display.

## Privacy rules

The display should not show:

- private calendar details
- sensitive family notes
- private guest/helper information
- anything restricted to adult/admin roles

## Constraints

E-paper screens usually work best with:

- simple layouts
- low image complexity
- infrequent refreshes
- high contrast
- short text

## Later improvements

- weather summary
- school/work reminders
- shared asset bookings
- QR code to open the mobile app
- manual household announcement mode
