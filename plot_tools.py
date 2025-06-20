# -------------------------------------------------------------------------------------------------
# Tools used across all reports
# -------------------------------------------------------------------------------------------------

# cspell:ignore APAC Aptos automargin categoryarray categoryorder EMEA Futurum gridcolor
# cspell:ignore gridwidth insidetextanchor LATAM linecolor OxmlElement qn showgrid showline
# cspell:ignore sizex sizey textangle textfont textposition tickangle tickfont tickmode
# cspell:ignore twips xaxes xaxis yaxes yaxis yref


import math
import os

import geo_tools
import os_tools
import plotly.graph_objects as go  # type: ignore
import plotly.io as pio  # type: ignore
from common_data import (
    BANANA_YELLOW,
    CHART_HEIGHT,
    CHART_WIDTH,
    COPYRIGHT,
    FOR_FUTURUM,
    FUTURUM_COLORS,
    FUTURUM_LOGO_PATH,
    HARVARD_CRIMSON,
    ROYAL_BLUE,
    SHOW_CHART_LOGOS,
    SHOW_FIGURE_NUMBERS,
    SHOW_SUTOR_GROUP_COPYRIGHT,
    SHOW_TITLE,
    SUTOR_GROUP_LOGO_PATH,
)
from PIL import Image
from sty import fg  # type: ignore

# import time


BACKGROUND_COLOR = "white"
# BACKGROUND_COLOR = "rgba(0,0,0,0)"  # transparent

# -------------------------------------------------------------------------------------------------
# Color tools
# -------------------------------------------------------------------------------------------------

# https://colorkit.co/
# https://plotly.com/python/discrete-color/

# import random

# import plotly.colors as colors  # type: ignore


def interpolate_color(start_hex, end_hex, steps):
    if FOR_FUTURUM:
        color_list = steps * FUTURUM_COLORS
        return color_list[:steps]

    # Generated by Perplexity

    # Convert hex to RGB
    start_rgb = tuple(int(start_hex[i : i + 2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end_hex[i : i + 2], 16) for i in (1, 3, 5))

    # Calculate step size for each color component
    step_r = (end_rgb[0] - start_rgb[0]) / (steps - 1)
    step_g = (end_rgb[1] - start_rgb[1]) / (steps - 1)
    step_b = (end_rgb[2] - start_rgb[2]) / (steps - 1)

    # Generate interpolated colors
    color_list = []
    for i in range(steps):
        r = int(start_rgb[0] + step_r * i)
        g = int(start_rgb[1] + step_g * i)
        b = int(start_rgb[2] + step_b * i)
        color_list.append(f"#{r:02x}{g:02x}{b:02x}")

    return color_list


def generate_color_palette(minimum_length: int) -> list[str]:
    if minimum_length < 4:
        palette = generate_color_palette(20)
        return [palette[3], HARVARD_CRIMSON, ROYAL_BLUE]
    palette = (
        interpolate_color(BANANA_YELLOW, HARVARD_CRIMSON, 1 + minimum_length // 2)
        + interpolate_color(HARVARD_CRIMSON, ROYAL_BLUE, 1 + minimum_length // 2)[1:]
    )
    return palette


# -------------------------------------------------------------------------------------------------
# Plotting tools
# -------------------------------------------------------------------------------------------------

X_AXIS_TICK_SIZE = 32


if FOR_FUTURUM:
    LOGO = Image.open(FUTURUM_LOGO_PATH)
    STRETCH = 0.10
else:
    LOGO = Image.open(SUTOR_GROUP_LOGO_PATH)
    STRETCH = 0.14


def y_max_with_rounder(rounder, y_max):
    if y_max % rounder == 0:
        y_max += rounder
    else:
        y_max = int(rounder * math.ceil(y_max / float(rounder)))

    return y_max


def set_figure_defaults(figure, figure_count, title, title_x, title_y, total_companies):
    if FOR_FUTURUM:
        PLOT_FONT_FAMILY = "Arial, Aptos, san-serif, IBM Plex Sans"
    else:
        PLOT_FONT_FAMILY = "Aptos, Arial, san-serif, IBM Plex Sans"

    # General settings

    if title:
        print(f"Creating chart {fg.green}'{title}'{fg.rs}")

    figure.update_layout(
        font_family=PLOT_FONT_FAMILY,
        font_color="black",
        font_size=24,
        autosize=False,
        width=CHART_WIDTH,
        height=CHART_HEIGHT,
        paper_bgcolor=BACKGROUND_COLOR,
        plot_bgcolor=BACKGROUND_COLOR,
    )

    # Axes

    figure.update_xaxes(
        type="category",
        showline=True,
        linewidth=1,
        linecolor="black",
        tickmode="linear",
        tickfont=dict(size=X_AXIS_TICK_SIZE),
        tickangle=-45,
    )

    figure.update_yaxes(showgrid=True, gridwidth=1, gridcolor="gray")
    figure.update_yaxes(showline=True, linewidth=1, linecolor="black")

    figure.update_traces(textfont_size=X_AXIS_TICK_SIZE, textangle=0, textposition="outside")

    # Titles

    font_spec = dict()
    font_spec["family"] = PLOT_FONT_FAMILY
    font_spec["size"] = 36
    font_spec["weight"] = "bold"
    font_spec["color"] = "black"

    copyright_style = "font-size: 22pt; font-weight: normal; font-style: italic;"

    if SHOW_FIGURE_NUMBERS:
        figure.update_layout(
            xaxis_title=title_x + f"<br><br>Figure {figure_count}",
            xaxis_title_font=dict(weight="bold", size=36),
        )

    elif SHOW_SUTOR_GROUP_COPYRIGHT:
        figure.update_layout(
            xaxis_title=f"{title_x}<br><br><span style='{copyright_style}'>{COPYRIGHT}</span>",
            xaxis_title_font=dict(weight="bold", size=36),
        )
    else:
        figure.update_layout(xaxis_title=title_x, xaxis_title_font=dict(weight="bold", size=36))

    figure.update_layout(yaxis_title=title_y, yaxis_title_font=dict(weight="bold", size=36))

    font_spec["size"] = 38
    font_spec["weight"] = "bold"

    if total_companies > 0:
        if SHOW_TITLE and title:
            figure.update_layout(title={"text": title, "x": 0.5, "automargin": False, "font": font_spec})
            figure.update_layout(
                title=dict(
                    subtitle=dict(
                        text=f"Total Number of Distinct Companies = {total_companies}",
                        font=font_spec,
                    )
                )
            )
        else:
            figure.update_layout(
                title={
                    "text": f"Total Number of Distinct Companies = {total_companies}",
                    "x": 0.5,
                    "automargin": False,
                    "font": font_spec,
                }
            )
            # figure.update_layout(
            #     title=dict(
            #         subtitle=dict(
            #             text=f"Total Number of Distinct Companies = {total_companies}", font=font_spec
            #         )
            #     )
            # )
    elif SHOW_TITLE and title:
        figure.update_layout(title={"text": title, "x": 0.5, "automargin": False, "font": font_spec})

    # Margins

    figure.update_layout(
        margin=dict(
            l=50,  # Left margin
            r=20,  # Right margin
            # t=200,  # Top margin
            # b=60,  # Bottom margin
        )
    )

    # Add centered annotation at the bottom, outside the plot area
    # if SHOW_SUTOR_GROUP_COPYRIGHT:
    #     figure.add_annotation(
    #         text=COPYRIGHT,
    #         xref="paper",
    #         yref="paper",
    #         x=0.5,
    #         y=-0.3,  # Centered horizontally, at the very bottom
    #         xanchor="center",
    #         yanchor="bottom",
    #         showarrow=False,
    #         font=dict(size=24),
    #     )

    #     figure.update_layout(
    #         margin=dict(
    #             b=500,  # Bottom margin
    #         )
    #     )

    # Logo

    # if SHOW_CHART_LOGOS:
    #     figure.add_layout_image(
    #         dict(
    #             source=LOGO,
    #             xref="paper",
    #             yref="paper",
    #             x=1.0,
    #             y=1.1,
    #             sizex=STRETCH,
    #             sizey=STRETCH,
    #             sizing="contain",
    #             opacity=1.0,
    #             xanchor="right",
    #             yanchor="top",
    #             layer="above",
    #         )
    #     )


def companies_in_countries_chart(
    xs, ys, figure_count, title, title_x, title_y, total_companies, rounder, chart_file
):
    print("Building companies in countries chart: ", end="")
    os_tools.start_timer()

    fig = go.Figure(
        [
            go.Bar(
                x=xs,
                y=ys,
                text=[str(y) for y in ys],
                marker={"color": generate_color_palette(len(xs)), "line": dict(color="black", width=1)},
                textposition="outside",
                insidetextanchor="middle",
            )
        ]
    )

    set_figure_defaults(fig, figure_count, title, title_x, title_y, total_companies)

    if ys:
        max_ys = max(ys)
    else:
        max_ys = 0

    fig.update_layout(yaxis=dict(range=[0, y_max_with_rounder(rounder, max_ys)]))

    # fig.write_image(chart_file, format="png", engine="kaleido")
    pio.write_image(fig, chart_file)
    if not os.path.exists(chart_file):
        os_tools.terminating_error(f"Chart file '{chart_file}' was not created.")

    print(f"{os_tools.end_timer()} seconds")

    return fig


def companies_in_country_region_chart(
    country_regions,
    xs,
    ys,
    max_ys,
    figure_count,
    title,
    title_x,
    title_y,
    total_companies,
    rounder,
    chart_file,
):
    print(f"Building companies in {country_regions} chart: ", end="")
    os_tools.start_timer()

    fig = go.Figure(
        [
            go.Bar(
                x=xs,
                y=ys,
                text=[str(y) for y in ys],
                marker={"color": generate_color_palette(len(xs)), "line": dict(color="black", width=1)},
                textposition="outside",
                insidetextanchor="middle",
            )
        ]
    )

    set_figure_defaults(fig, figure_count, title, title_x, title_y, total_companies)

    # if ys:
    #     max_ys = max(ys)
    # else:
    #     max_ys = 0

    fig.update_layout(yaxis=dict(range=[0, y_max_with_rounder(rounder, max_ys)]))

    fig.update_layout(
        yaxis=dict(
            dtick=1  # Show a tick for every integer
        )
    )

    # fig.write_image(chart_file, format="png", engine="kaleido")
    pio.write_image(fig, chart_file)

    print(f"{os_tools.end_timer()} seconds")

    return fig


def companies_in_regions_chart(
    xs, ys, figure_count, title, title_x, title_y, total_companies, rounder, chart_file
):
    print("Building companies in regions chart: ", end="")
    os_tools.start_timer()

    region_order = geo_tools.get_region_abbreviations()
    assert len(xs) == len(region_order)

    new_ys = []

    for region in region_order:
        ix = xs.index(region)
        new_ys.append(ys[ix])

    fig = go.Figure(
        [
            go.Bar(
                x=region_order,
                y=new_ys,
                text=[str(y) for y in new_ys],
                marker={
                    "color": generate_color_palette(len(region_order)),
                    "line": dict(color="black", width=1),
                },
                textposition="outside",
                insidetextanchor="middle",
            )
        ]
    )

    set_figure_defaults(fig, figure_count, title, title_x, title_y, total_companies)

    if new_ys:
        max_ys = max(new_ys)
    else:
        max_ys = 0

    fig.update_layout(yaxis=dict(range=[0, y_max_with_rounder(rounder, max_ys)]))

    fig.update_layout(xaxis=dict(categoryorder="array", categoryarray=region_order))  # likely redundant

    # we draw a vertical line after the NA bar

    post_na_position = region_order.index("NA") + 0.5

    fig.update_layout(
        shapes=[
            dict(
                type="line",
                x0=post_na_position,
                y0=0,
                x1=post_na_position,
                y1=max(ys),
                line=dict(color="Gray", width=8),
            )
        ]
    )

    # fig.write_image(chart_file, format="png", engine="kaleido")
    pio.write_image(fig, chart_file)

    print(f"{os_tools.end_timer()} seconds")

    return fig


def years_founded_chart(xs, ys, figure_count, title, title_x, title_y, total_companies, rounder, chart_file):
    print("Building companies and years founded chart: ", end="")
    os_tools.start_timer()

    fig = go.Figure(
        [
            go.Bar(
                x=xs,
                y=ys,
                text=[str(y) for y in ys],
                marker={"color": generate_color_palette(len(xs)), "line": dict(color="black", width=1)},
                textposition="outside",
                insidetextanchor="middle",
            )
        ]
    )

    set_figure_defaults(fig, figure_count, title, title_x, title_y, total_companies)

    if ys:
        max_ys = max(ys)
    else:
        max_ys = 0

    fig.update_layout(yaxis=dict(range=[0, y_max_with_rounder(rounder, max_ys)]))

    # fig.write_image(chart_file, format="png", engine="kaleido")
    pio.write_image(fig, chart_file)

    print(f"{os_tools.end_timer()} seconds")

    return fig
