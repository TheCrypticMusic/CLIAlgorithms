from typing import Optional
import typer
from src.algorithms.binary_search import BinarySearch
from src.algorithms.linear_search import LinearSearch
import src.helpers.cli_helpers as cli_helpers

app = typer.Typer()

@app.command("binary_search")
def cli_binary_search(user_ordered_list: str, user_target: int):

    binary_search = BinarySearch(cli_helpers.to_list(user_ordered_list), int(user_target))

    while binary_search.is_found == False:
        cli_helpers.draw_binary_search_table(
            "Binary Search",
            binary_search.lower_bound,
            binary_search.upper_bound,
            binary_search.ordered_list,
            binary_search.ordered_list.index(binary_search.target),
            binary_search.find_mid_point(
                binary_search.lower_bound, binary_search.upper_bound
            ),
        )

        cli_helpers.draw_table_key(
            lower_bound=f"L - Lower Bound = {binary_search.lower_bound}",
            upper_bound=f"U - Upper Bound = {binary_search.upper_bound}",
            middle_point=f"M - Middle Point = {binary_search.find_mid_point(binary_search.lower_bound, binary_search.upper_bound)}",
            target=f"T - Target (Index) = {binary_search.ordered_list.index(binary_search.target)}",
        )
        binary_search.run(loop=False)


@app.command("linear_search")
def cli_linear_search(user_list: str, user_target: int):
    
    converted_user_list = cli_helpers.to_list(user_input=user_list)

    linear_search = LinearSearch(converted_user_list, user_target)

    while linear_search.is_found == False:

        cli_helpers.draw_linear_search_table("Linear Search",
                                            linear_search.list,
                                            linear_search.current_number,
                                            linear_search.target,
                                            linear_search.list_index,
                                            linear_search.target_index
                                             )

        cli_helpers.draw_table_key(current_number=f"C - Current = {linear_search.current_number}",
                                   list_index=f"I - Current Number Index = {linear_search.list_index}",
                                   target=f"T - Target = {linear_search.target}",
                                   target_index=f"TI - Target Index = {linear_search.target_index}")       
        linear_search.run(loop=False)


@app.command()
def test1():
    print("Hello")


def main():
    app()
