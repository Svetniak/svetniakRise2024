local wezterm = require("wezterm")

local config = {}
-- use config builder objects if possible
if wezterm.config_builder then
	config = wezterm.config_builder()
end

config.color_scheme = "Tokyo Night"
config.font = wezterm.font_with_fallback({
	{ family = "SauceCodeProNerdFont", scale = 0.9, weight='Bold' },
	{ family = "RobotoMono Nerd Font", scale = 0.9 },
})
config.window_background_opacity = 0.7
config.window_decorations = "RESIZE"
config.scrollback_lines = 3000
config.default_workspace = "home"

config.inactive_pane_hsb = {
	saturation = 0.5,
	brightness = 0.5,
}

config.use_fancy_tab_bar = false

return config
