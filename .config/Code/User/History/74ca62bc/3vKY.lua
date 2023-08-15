rule = {
    matches = {
        {
            { "node.name", "equals", "alsa_output." },
        },
    },
    apply_properties = {
        ["node.description"] = "Laptop",
    },
}

table.insert(alsa_monitor.rules, rule)
