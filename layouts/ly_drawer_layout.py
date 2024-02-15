from components.c_tabs_group import create_tabs_group
import dash_mantine_components as dmc


def create_drawer_layout():
    return dmc.Drawer(
        create_tabs_group(),
        id="drawer-control",
        position="right",
        # padding="md",
        size="65%",
        zIndex=10000,
        className="drawer-layout",
        closeOnClickOutside=True,
        classNames="drawer-tab-layout",
    )
