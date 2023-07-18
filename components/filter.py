from shiny import ui


def product_filter():
    return ui.tags.div(
        ui.tags.h5(
            "Product",
            class_="filter_label text-sm font-medium",
        ),
        ui.tags.div(
            class_="dropdown text-sm font-medium",
        ),
        class_="flex items-center",
    )


def country_filter():
    return ui.tags.div(
        ui.tags.h5(
            "Country",
            class_="filter_label text-sm font-medium",
        ),
        ui.tags.div(
            class_="dropdown text-sm font-medium",
        ),
        class_="ml-8 flex items-center",
    )
