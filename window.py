from defaults import *

class Window(Gtk.ApplicationWindow):
    def __init__(self, **kargs):
        super().__init__(**kargs)
        self.set_default_size(WINDOW_DEF_WIDTH, WINDOW_DEF_HEIGHT)

        # Header
        header_bar = Gtk.HeaderBar()
        self.set_titlebar(header_bar)
        run_button = Gtk.Button(label='Run')
        run_button.connect('clicked', self.run_graph)
        header_bar.pack_start(run_button)
        new_button = Gtk.Button(label='＋')
        new_button.connect('clicked', self.start_new_tab)
        header_bar.pack_end(new_button)
        self.p = None

        self.tabs = Gtk.Notebook()
        self.set_child(self.tabs)
        self.start_new_tab(None)

    def start_new_tab(self, _a):
        page = Gtk.Grid(column_homogeneous=True, row_homogeneous=True,
                             column_spacing=10, row_spacing=10)
        page.set_hexpand(True)
        page.set_vexpand(True)
        input = Gtk.Entry()
        input.set_max_length(10)
        input.set_placeholder_text("Enter Int")
        input.set_hexpand(True)
        graph_placeholder = Gtk.Label(label='Enter your number then\nhit `Run` to generate Graph')
        graph_placeholder.set_vexpand(True)
        page.attach(input, 0, 0, 1, 1)
        page.attach(graph_placeholder, 0, 1, 1, 9)
        self.tabs.append_page(page, Gtk.Label(label='New Test'))
        self.tabs.set_current_page(self.tabs.get_n_pages()-1)

    def run_graph(self, _a):
        current_page = self.tabs.get_nth_page(self.tabs.get_current_page())
        try:
            seq = int(current_page.get_first_child().get_buffer().get_text())
            current_page.remove(current_page.get_child_at(0,1))
            self.tabs.set_tab_label_text(current_page, "Seq: "+str(seq))
            da2 = Gtk.DrawingArea()
            da2.set_draw_func(on_draw, aliquot(seq))
            da2.queue_draw()
            def refresh_screen():
                da2.queue_draw()
                GLib.timeout_add(1000 / 60, refresh_screen)
            GLib.timeout_add(1000 / 60, refresh_screen)
            current_page.attach(da2, 0, 1, 1, 9)
        except ValueError as e:
            alert = Gtk.AlertDialog()
            alert.set_buttons(["Okay"])
            alert.set_message("Error")
            alert.set_default_button(0)
            alert.set_detail("Please type an integer only")
            alert.show(self)
