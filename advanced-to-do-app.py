from flet import *

def main(page: Page):
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK ='#eb06ff'

    

    

    create_task_view = Container(
        content= Container(
            on_click=lambda _ :page.go('/'),
            height=40,
            width=40,
            content=Text('X')
        )
    )

    tasks = Column (
        width= 400,
        scroll='auto',
        controls=[
            #
        ]
    )
    for i in range(10):
        tasks.controls.append(
            Container(
                height=50,
                width=300,
                bgcolor='red'
            ),
        )  


    categories_card = Row(
        scroll='auto'
    )
    categories = ['Buisness', 'Family', 'Friends']
    for i, category in enumerate (categories):
        categories_card.controls.append(
            Container(
                bgcolor=BG, 
                border_radius=20,
                height=110, 
                width=170,
                padding=15,
                content=Column(
                    controls=[
                        Text('40 Tasks'),
                        Text(category),
                        Container(
                            width=160,
                            height=5,
                            bgcolor='white12',
                            border_radius=20,
                            padding=padding.only(right=i*30),
                            content=Container(
                                bgcolor=PINK,
                            ),
                        )
                    ]
                )
            )
        )

    first_page_contents = Container(
        content=Column(
            controls=[
                Row(
                    alignment='spaceBetween',
                    controls=[
                      Container(
                          content=Icon(
                              icons.MENU)),
                      Row(
                          controls=[
                              Icon(icons.SEARCH),
                              Icon(icons.NOTIFICATION_ADD_OUTLINED),
                          ]
                      ),          
                    ]
                ),
                Container(height=20),
                Text(
                    value='Whats\' up, Kasun!'
                ),
                Text(
                    value='CATEGORIES'
                ),
                Container(
                    padding=padding.only(top=10, bottom=20),
                    content=categories_card
                ),
                Container(height=20),
                Text("TODAY'S TASK"),
                Stack(
                    controls=[
                        tasks,
                        FloatingActionButton(
                            icon = icons.ADD, on_click= lambda _ : page.go
                            ('/create_task')
                        ),
                    ]
                )
            ]
        )
    )


    page_1 = Container()

    page_2 = Row(
        controls=[
            Container(
            width=370,
            height = 770,
            bgcolor=FG,
            border_radius=35,
            padding=padding.only(
                top=50, left=20,
                right=20,bottom=5,
            ),
            content=Column(
                controls=[
                   first_page_contents 
                ]
            )
        )
      ]
    )

    container = Container(
        width=370, 
        height=770, 
        bgcolor= BG,
        border_radius=35,
        content=Stack(
            controls=[
                page_1,
                page_2
            ]
        )
    )

    pages = {
        '/': View(
            "/",
            [
                container
            ],
        ),

        '/create_task' : View(
            "/create_task",
            [
                create_task_view
            ]
        )
    }

    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )

    page.add(container)

    page.on_route_change = route_change
    page.go(page.route)

app(target=main)