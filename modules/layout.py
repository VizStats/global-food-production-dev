from shiny import ui
from components import svg, filter


def introduction() -> ui.tags.main:
    return ui.tags.main(
        ui.h1("Introduction", class_="text-lg font-bold "), class_="h-96"
    )


def layout() -> ui.tags.main:
    return ui.tags.main(
        ui.tags.div(
            # dashboard nav section
            ui.tags.section(
                # add logo and title
                ui.tags.div(
                    ui.tags.div(svg.vizstats_logo(), class_="header_logo xl:hidden"),
                    ui.tags.div(
                        svg.vizstats_full_logo(), class_="header_logo hidden xl:block"
                    ),
                    ui.tags.div(class_="stroke_divider"),
                    ui.tags.h4(
                        "Global Food Production", class_="text-2xl font-semibold"
                    ),
                    class_="title flex justify-between items-center",
                ),
                # add filters
                ui.tags.div(
                    filter.product_filter(),
                    filter.country_filter(),
                    class_="filters flex flex-wrap justify-between items-center",
                ),
                class_="header p-4 mb-2 flex flex-wrap justify-between items-center",
            ),
            # dashboard main section
            ui.tags.section(
                ui.tags.div(
                    ui.tags.div(class_="map"),
                    ui.tags.div(class_="main_children"),
                    class_="main_child1",
                ),
                ui.tags.div(
                    ui.tags.div(class_="main_children"),
                    ui.tags.div(class_="main_children"),
                    class_="main_child2",
                ),
                class_="main_dashboard mx-6 mb-6",
            ),
            class_="dashboard dashboard_layout",
        ),
        class_="dashboard_container flex justify-center items-center",
    )
