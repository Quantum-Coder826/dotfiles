use druid::widget::Label;
use druid::{AppLauncher, Widget, WindowDesc};

fn build_ui() -> impl Widget<()> {
    
}

fn main() {
    let main_window = WindowDesc::new(build_ui())
        .window_size((100.0, 100.0))
        .title("rusty mines");
    let initial_data = ();

    AppLauncher::with_window(main_window)
        .launch(initial_data)
        .expect("Failed to launch application");
}