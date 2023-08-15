rule = {
    matches = {
        {
            { "node.name", "equals", "alsa_output.HyperX Virtual Surround Sound" },
        },
    },
    apply_properties = {
        ["node.description"] = "Laptop",
    },
}

table.insert(alsa_monitor.rules, rule)
