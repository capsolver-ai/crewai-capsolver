# Architecture

This is an adapter, not a second solving engine. It owns framework registration, compatibility, examples, and adapter tests. capsolver-agent owns canonical tool contracts. capsolver-core owns detection, parameter extraction, solving, fill-back, retries, and errors. The application owns authorization, compliance, rate limits, data handling, and agent policy.

Do not copy solving or DOM-injection logic into adapters.
