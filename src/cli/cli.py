from typing import Optional
import typer

from src.algorithms.binary_search import BinarySearch
import src.helpers.cli_helpers as cli_helpers

app = typer.Typer()

@app.command("binary_search")
def cli_binary_search():

    binary_list = BinarySearch([1, 5, 7, 9, 10, 11, 13, 14, 17, 19, 24, 27, 28, 29, 35, 38, 41, 42, 44], 24)

    while binary_list.is_found == False:
        cli_helpers.draw_binary_search_table("Binary Search", binary_list.lower_bound, binary_list.upper_bound, binary_list.ordered_list, binary_list.ordered_list.index(binary_list.target), binary_list.find_mid_point(binary_list.lower_bound, binary_list.upper_bound))    
        binary_list.run(loop=False)
    
@app.command()
def test1():
    print("Hello")

def main(): 
    app()