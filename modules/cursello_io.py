'''
cursello_io.py

IO/handling module for cursello. Centers around curses-style inputs.

Douglas J. Smith
12/28/17
'''
import curses
'''
debug - take a string and a screen and display the string at the base of the
  window, useful for alerts or certain I/O display.

INPUT:
stdscr:Window[curses] - screen object.
msg:String - message to be displayed.
style:Integer - curses macro code for styling input.
'''
def debug(stdscr, msg, style=curses.A_DIM):
  stdscr.addstr(curses.LINES - 1, 0, msg, style)


'''
StringInput - take a string entered by the user in a command bar, return the
properly-processed result.

INPUT:
screen:Window[curses] - window object that bar will be displayed within
prompt:String - string that is used to request input. Prompt is flashed before
  input and disappears when the user starts typing. Must be included, otherwise
  a confusingly blank box is flashed.

OUTPUT:
result:String - processed version of user's input
'''
def BarInput(cursello, prompt):
  screen = cursello.win

  screen_yx = screen.getmaxyx()

  #Reactivate the cursor
  curses.curs_set(1)
  curses.echo()

  # Display the prompt message
  screen.addstr(screen_yx[0] - 1, 0, prompt)
  # screen.refresh(cursello.pad_pos_y,cursello.pad_pos_x, 0,0, screen_yx[0]-1, screen_yx[1]-1)
  screen.refresh()

  # Get user input after the prompt message
  st = screen.getstr(screen_yx[0] - 1, len(prompt))

  # reset things
  curses.curs_set(0)
  curses.noecho()
  screen.clear()
  screen.refresh()

  # return string
  return st.strip()
