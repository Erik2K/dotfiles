return {
	{
		"stevearc/conform.nvim",
		opts = require("configs.conform"),
	},

	{
		"neovim/nvim-lspconfig",
		config = function()
			require("configs.lspconfig")
		end,
	},

	{
		"nvim-tree/nvim-tree.lua",
		opts = {
			filters = {
				dotfiles = false,
			},
			git = {
				enable = true,
				ignore = false,
			},
			renderer = {
				highlight_git = true,
			},
		},
	},

	{
		"nvim-telescope/telescope.nvim",
		opts = {
			pickers = {
				find_files = {
					hidden = true,
					no_ignore = true,
				},
			},
		},
	},
}
