from typing import Optional
import typer

from src.algorithms.binary_search import BinarySearch
import src.helpers.cli_helpers as cli_helpers

app = typer.Typer()

@app.command("binary_search")
def cli_binary_search(user_ordered_list: str, user_target: int):

    binary_list = BinarySearch(cli_helpers.to_list(user_ordered_list), int(user_target))

    while binary_list.is_found == False:
        cli_helpers.draw_binary_search_table(
            "Binary Search",
            binary_list.lower_bound,
            binary_list.upper_bound,
            binary_list.ordered_list,
            binary_list.ordered_list.index(binary_list.target),
            binary_list.find_mid_point(
                binary_list.lower_bound, binary_list.upper_bound
            ),
        )

        cli_helpers.draw_table_key(
            lower_bound=f"L - Lower Bound = {binary_list.lower_bound}",
            upper_bound=f"U - Upper Bound = {binary_list.upper_bound}",
            middle_point=f"M - Middle Point = {binary_list.find_mid_point(binary_list.lower_bound, binary_list.upper_bound)}",
            target=f"T - Target (Index) = {binary_list.ordered_list.index(binary_list.target)}",
        )
        binary_list.run(loop=False)


@app.command()
def test1():
    print("Hello")


def main():
    app()
