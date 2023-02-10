from typing import Optional
import typer

from src.algorithms.binary_search import BinarySearch
import src.helpers.cli_helpers as cli_helpers

app = typer.Typer()

# TODO: Get input from user.


@app.command("binary_search")
def cli_binary_search(user_ordered_list: str, user_target: int):

    
    # pre_made_list = [1, 5, 7, 9, 10, 11, 13, 14, 17, 19, 24, 27, 28, 29, 35, 38, 41, 42, 44],
    # pre_made_target = 14
    
    

    binary_list = BinarySearch(cli_helpers.to_list(user_ordered_list), int(user_target))
    # print(binary_list.ordered_list.index(binary_list.target))
    print(binary_list.ordered_list, binary_list.target)
    # while binary_list.is_found == False:
    #     cli_helpers.draw_binary_search_table(
    #         "Binary Search",
    #         binary_list.lower_bound,
    #         binary_list.upper_bound,
    #         binary_list.ordered_list,
    #         binary_list.ordered_list.index(binary_list.target),
    #         binary_list.find_mid_point(
    #             binary_list.lower_bound, binary_list.upper_bound
    #         ),
    #     )

    #     cli_helpers.draw_table_key(
    #         lower_bound=f"L - Lower Bound = {binary_list.lower_bound}",
    #         upper_bound=f"U - Upper Bound = {binary_list.upper_bound}",
    #         middle_point=f"M - Middle Point = {binary_list.find_mid_point(binary_list.lower_bound, binary_list.upper_bound)}",
    #         target=f"T - Target (Index) = {binary_list.ordered_list.index(binary_list.target)}"
    #     )
    #     binary_list.run(loop=False)


@app.command()
def test1():
    print("Hello")


def main():
    app()
