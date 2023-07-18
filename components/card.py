from shiny import ui
from htmltools import HTML


def card(title: str, description: str):
    """
    Generate an HTML card component with a title, description, and a "Read more" link.

    Args:
        title (str): The title of the card.
        description (str): The description of the card.

    Returns:
        str: The HTML structure representing the card component.

    Example:
        >>> card("Example Title", "This is an example description.")
        '<div class="max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow">...</div>'
    """
    TITLE = str(title)

    DESCRITION = str(description)

    card = ui.tags.div(
        ui.tags.div(
            ui.tags.a(
                ui.tags.h5(
                    TITLE,
                    class_="mb-2 text-2xl font-bold tracking-tight text-gray-900",
                ),
                href="#",
            ),
            ui.tags.p(
                DESCRITION,
                class_="mb-3 font-normal text-gray-700",
            ),
            ui.tags.a(
                ui.tags.h5(
                    "Read more",
                    ui.tags.svg(
                        HTML(
                            "<path stroke='currentColor' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M1 5h12m0 0L9 1m4 4L9 9'/>"
                        ),
                        aria_hidden="true",
                        xmlns="http://www.w3.org/2000/svg",
                        fill="none",
                        viewBox="0 0 14 10",
                        class_="w-3.5 h-3.5 ml-2",
                    ),
                    class_="inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300",
                ),
                href="#",
            ),
            class_="max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow",
        )
    )
    return card


def card_link(title: str, description: str):
    TITLE = str(title)
    DESCRIPTION = str(description)
    card_link = ui.tags.a(
        ui.tags.h5(
            TITLE,
            class_="mb-2 text-2xl font-bold tracking-tight text-gray-900",
        ),
        ui.tags.p(
            DESCRIPTION,
            class_="font-normal text-gray-700",
        ),
        href="#",
        class_="block max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow hover:bg-gray-100 ",
    )
    return card_link


def help_card():
    help_card = ui.tags.div(
        ui.tags.svg(
            HTML(
                '<path d="M18 5h-.7c.229-.467.349-.98.351-1.5a3.5 3.5 0 0 0-3.5-3.5c-1.717 0-3.215 1.2-4.331 2.481C8.4.842 6.949 0 5.5 0A3.5 3.5 0 0 0 2 3.5c.003.52.123 1.033.351 1.5H2a2 2 0 0 0-2 2v3a1 1 0 0 0 1 1h18a1 1 0 0 0 1-1V7a2 2 0 0 0-2-2ZM8.058 5H5.5a1.5 1.5 0 0 1 0-3c.9 0 2 .754 3.092 2.122-.219.337-.392.635-.534.878Zm6.1 0h-3.742c.933-1.368 2.371-3 3.739-3a1.5 1.5 0 0 1 0 3h.003ZM11 13H9v7h2v-7Zm-4 0H2v5a2 2 0 0 0 2 2h3v-7Zm6 0v7h3a2 2 0 0 0 2-2v-5h-5Z"/>'
            ),
            class_="w-7 h-7 text-gray-500 mb-3",
            aria_hidden="true",
            xmlns="http://www.w3.org/2000/svg",
            fill="currentColor",
            viewBox="0 0 20 20",
        ),
        ui.tags.a(
            ui.tags.h5(
                "Need a help in Claim?",
                class_="mb-2 text-2xl font-semibold tracking-tight text-gray-900",
            ),
            href="#",
        ),
        ui.tags.p(
            "Go to this step by step guideline process on how to certify for your weekly benefits:",
            class_="mb-3 font-normal text-gray-500",
        ),
        ui.tags.a(
            "See our guideline",
            ui.tags.svg(
                HTML(
                    '<path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11v4.833A1.166 1.166 0 0 1 13.833 17H2.167A1.167 1.167 0 0 1 1 15.833V4.167A1.166 1.166 0 0 1 2.167 3h4.618m4.447-2H17v5.768M9.111 8.889l7.778-7.778"/>'
                ),
                class_="w-3 h-3 ml-2.5",
                aria_hidden="true",
                xmlns="http://www.w3.org/2000/svg",
                fill="none",
                viewBox="0 0 18 18",
            ),
            href="#",
            class_="inline-flex items-center text-blue-600 hover:underline",
        ),
        class_="max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow",
    )
    return help_card


def flex_card():
    flex_card = ui.tags.a(
        ui.tags.img(
            class_="object-cover w-full rounded-t-lg h-96 md:h-auto md:w-48 md:rounded-none md:rounded-l-lg",
            src="/docs/images/blog/image-4.jpg",
            alt="",
        ),
        ui.tags.div(
            ui.tags.h5(
                "Noteworthy technology acquisitions 2021",
                class_="mb-2 text-2xl font-bold tracking-tight text-gray-900",
            ),
            ui.tags.p(
                "Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order.",
                class_="mb-3 font-normal text-gray-700",
            ),
            class_="flex flex-col justify-between p-4 leading-normal",
        ),
        href="#",
        class_="flex flex-col items-center bg-white border border-gray-200 rounded-lg shadow md:flex-row md:max-w-xl hover:bg-gray-100",
    )
    return flex_card
