"""
01_generate_dataset.py
Generates a synthetic Flutter Q&A dataset in Alpaca instruction format.

The dataset contains ~1100 samples across three categories:
  - Basic (330): Flutter overview, Dart basics, widget types, hot reload
  - Intermediate (440): Widget lifecycle, navigation, layouts, forms, animations
  - Advanced (330): State management, performance, platform channels, testing, CI/CD

Each sample follows the schema:
  { "instruction": str, "input": "", "output": str }

Output: data/flutter_qa_raw.json
"""

import json
import os


def generate_basic_questions():
    """Generate basic-level Flutter Q&A pairs."""
    return [
        # Flutter Overview
        {
            "instruction": "What is Flutter?",
            "input": "",
            "output": "Flutter is an open-source UI software development kit created by Google. It allows developers to build natively compiled applications for mobile, web, and desktop from a single codebase using the Dart programming language. Flutter uses a widget-based architecture and its own rendering engine for consistent UI across platforms."
        },
        {
            "instruction": "What are the main advantages of using Flutter for app development?",
            "input": "",
            "output": "Flutter offers several advantages: a single codebase for multiple platforms (iOS, Android, web, desktop), hot reload for fast development cycles, a rich set of customizable widgets, excellent performance due to direct compilation to native code, and a strong community with extensive package support through pub.dev."
        },
        {
            "instruction": "What is the Dart programming language?",
            "input": "",
            "output": "Dart is a client-optimized programming language developed by Google. It is the primary language used for building Flutter applications. Dart supports both ahead-of-time (AOT) and just-in-time (JIT) compilation, offers strong typing with type inference, async/await support, and a garbage collector for memory management."
        },
        {
            "instruction": "What is the difference between Flutter and React Native?",
            "input": "",
            "output": "Flutter uses Dart and renders UI with its own Skia engine, providing consistent visuals across platforms. React Native uses JavaScript and bridges to native UI components. Flutter generally offers better performance and pixel-perfect consistency, while React Native benefits from the larger JavaScript ecosystem and easier adoption for web developers."
        },
        {
            "instruction": "What is a Widget in Flutter?",
            "input": "",
            "output": "In Flutter, everything is a widget. A widget is an immutable description of part of the user interface. Widgets can be as simple as a text label or as complex as an entire screen. They form a tree structure where each widget is nested inside its parent, and Flutter rebuilds this tree whenever the UI needs to update."
        },
        {
            "instruction": "What is the difference between StatelessWidget and StatefulWidget?",
            "input": "",
            "output": "A StatelessWidget is immutable and does not maintain any mutable state — its build method depends only on its configuration. A StatefulWidget maintains mutable state via a companion State object and can rebuild its UI dynamically when state changes using setState(). Use StatelessWidget for static UI and StatefulWidget when the UI needs to change over time."
        },
        {
            "instruction": "What is StatefulWidget in Flutter?",
            "input": "",
            "output": "A StatefulWidget is a widget in Flutter that maintains mutable state. Unlike StatelessWidget, it can rebuild its UI dynamically when its internal state changes during runtime using the setState() method. It consists of two classes — the StatefulWidget class itself and a corresponding State class that holds the mutable state."
        },
        {
            "instruction": "What is StatelessWidget in Flutter?",
            "input": "",
            "output": "A StatelessWidget is a widget that does not require mutable state. It is immutable, meaning once built, it cannot change its appearance based on internal state changes. Its build method is called only when the widget is first inserted into the tree or when its parent provides new configuration. Examples include Text, Icon, and IconButton widgets."
        },
        {
            "instruction": "What is hot reload in Flutter?",
            "input": "",
            "output": "Hot reload is a feature in Flutter that allows developers to see code changes reflected in the running app almost instantly without losing the current application state. It works by injecting updated source code into the running Dart VM. This significantly speeds up the development cycle by eliminating the need for full app restarts during UI tweaks."
        },
        {
            "instruction": "What is the difference between hot reload and hot restart in Flutter?",
            "input": "",
            "output": "Hot reload injects updated code into the running Dart VM and preserves the current app state, making it nearly instantaneous. Hot restart, on the other hand, completely restarts the app from scratch, resetting all state. Hot reload is used for UI changes, while hot restart is needed when changes affect app initialization, global variables, or static fields."
        },
        {
            "instruction": "What is the pubspec.yaml file in Flutter?",
            "input": "",
            "output": "The pubspec.yaml file is the configuration file for a Flutter/Dart project. It defines the project name, description, version, SDK constraints, dependencies, dev dependencies, and assets. Flutter uses this file to manage packages from pub.dev and to locate resources like images and fonts that the app uses."
        },
        {
            "instruction": "What is the purpose of the main() function in a Flutter app?",
            "input": "",
            "output": "The main() function is the entry point of a Flutter application. It typically calls runApp() with the root widget of the application. The runApp() function takes the given widget, makes it the root of the widget tree, and schedules a frame to render the UI on screen."
        },
        {
            "instruction": "What is the MaterialApp widget in Flutter?",
            "input": "",
            "output": "MaterialApp is a convenience widget that wraps several widgets commonly required for Material Design applications. It provides theming, navigation routing, localization, and other app-level configurations. It sets up the Navigator, Theme, and other inherited widgets that child widgets can access throughout the app."
        },
        {
            "instruction": "What is the Scaffold widget in Flutter?",
            "input": "",
            "output": "Scaffold is a Material Design layout widget that provides the basic visual structure for a screen. It offers slots for common UI elements like AppBar, Drawer, BottomNavigationBar, FloatingActionButton, and the main body content. It handles the layout positioning of these elements according to Material Design guidelines."
        },
        {
            "instruction": "What is the BuildContext in Flutter?",
            "input": "",
            "output": "BuildContext is a reference to the location of a widget in the widget tree. It is used to obtain references to themes, media queries, and other inherited widgets. Each widget has its own BuildContext, which becomes the parent of the BuildContext for child widgets. It is passed to the build method and is essential for looking up the widget tree."
        },
        {
            "instruction": "What is the widget tree in Flutter?",
            "input": "",
            "output": "The widget tree is the hierarchical structure of all widgets that make up a Flutter application's UI. Every widget is nested inside a parent widget, forming a tree from the root widget (usually MaterialApp) down to the smallest UI elements. Flutter traverses this tree to build the element tree and render tree for actual display."
        },
        {
            "instruction": "What are the different types of widgets in Flutter?",
            "input": "",
            "output": "Flutter widgets are primarily categorized as StatelessWidget (immutable, no internal state) and StatefulWidget (maintains mutable state). They can also be classified by function: layout widgets (Row, Column, Stack), input widgets (TextField, Checkbox), display widgets (Text, Image), and structural widgets (Scaffold, AppBar). Additionally, there are InheritedWidgets for passing data down the tree."
        },
        {
            "instruction": "What is the Container widget in Flutter?",
            "input": "",
            "output": "Container is a convenience widget that combines common painting, positioning, and sizing widgets. It can apply padding, margins, borders, background color, decoration, and constraints to its child widget. When no child is provided, Container tries to be as large as possible; with a child, it sizes itself to the child."
        },
        {
            "instruction": "What is the Text widget in Flutter?",
            "input": "",
            "output": "The Text widget displays a string of text with a single style. It can be customized using the style parameter with a TextStyle object to control font size, weight, color, and other typography properties. For rich text with multiple styles in a single widget, RichText or Text.rich can be used."
        },
        {
            "instruction": "What is the Column widget in Flutter?",
            "input": "",
            "output": "Column is a layout widget that arranges its children vertically in a single column. It does not scroll by default. The main axis is vertical and the cross axis is horizontal. You can control alignment using mainAxisAlignment and crossAxisAlignment properties. If children overflow the available space, Flutter will show an overflow warning."
        },
        {
            "instruction": "What is the Row widget in Flutter?",
            "input": "",
            "output": "Row is a layout widget that arranges its children horizontally in a single row. Its main axis is horizontal and cross axis is vertical. Like Column, it uses mainAxisAlignment and crossAxisAlignment for alignment control. It does not scroll and will show an overflow error if children exceed available horizontal space."
        },
        {
            "instruction": "What is the difference between mainAxisAlignment and crossAxisAlignment?",
            "input": "",
            "output": "mainAxisAlignment controls how children are positioned along the primary axis of a widget (vertical for Column, horizontal for Row). crossAxisAlignment controls positioning along the perpendicular axis. For example, in a Column, mainAxisAlignment.center centers children vertically, while crossAxisAlignment.center centers them horizontally."
        },
        {
            "instruction": "What is the Expanded widget in Flutter?",
            "input": "",
            "output": "Expanded is a widget that expands a child of a Row, Column, or Flex to fill available space along the main axis. It takes a flex parameter (default 1) to control the proportion of space allocated when multiple Expanded widgets compete for space. It is a shorthand for Flexible with FlexFit.tight."
        },
        {
            "instruction": "What is the SizedBox widget in Flutter?",
            "input": "",
            "output": "SizedBox is a widget that forces its child to have a specific width and/or height. If given a child, it forces the child to the specified dimensions. Without a child, it acts as a gap — commonly used to add spacing between widgets in a Row or Column instead of using padding."
        },
        {
            "instruction": "What is the Padding widget in Flutter?",
            "input": "",
            "output": "Padding is a widget that insets its child by the given EdgeInsets. It adds empty space around its child widget. EdgeInsets can be specified using constructors like EdgeInsets.all(), EdgeInsets.symmetric(), or EdgeInsets.only() for fine-grained control over padding on each side."
        },
        {
            "instruction": "What is the ListView widget in Flutter?",
            "input": "",
            "output": "ListView is a scrollable list widget that displays its children linearly. It has several constructors: ListView() for a small fixed list, ListView.builder() for large or infinite lists with lazy building, ListView.separated() for lists with separators between items, and ListView.custom() for custom child models. It is the most commonly used scrolling widget."
        },
        {
            "instruction": "What is the difference between ListView and ListView.builder?",
            "input": "",
            "output": "ListView creates all children at once, which is suitable for small lists. ListView.builder lazily builds children on demand as they scroll into view, making it efficient for large or infinite lists. ListView.builder requires an itemBuilder callback and optionally an itemCount, and only creates widgets that are currently visible."
        },
        {
            "instruction": "What is the GridView widget in Flutter?",
            "input": "",
            "output": "GridView is a scrollable 2D array of widgets. It displays items in a grid pattern and supports both fixed-count and max-extent-based column layouts via GridView.count and GridView.extent. Like ListView, it has a .builder constructor for lazy rendering of large datasets. It scrolls in one direction with items arranged in a grid."
        },
        {
            "instruction": "What is the Stack widget in Flutter?",
            "input": "",
            "output": "Stack is a layout widget that positions its children relative to its edges, allowing them to overlap. Children are painted in order, with the first child at the bottom. It uses Positioned widgets to place children at specific locations. Stack is useful for overlaying widgets, such as placing text over an image or creating custom layered layouts."
        },
        {
            "instruction": "What is the Positioned widget in Flutter?",
            "input": "",
            "output": "Positioned is a widget used inside a Stack to control where a child is placed. It allows specifying exact positions using top, right, bottom, left, width, and height properties. Only Positioned widgets or Align widgets can have precise control over their position within a Stack."
        },
        {
            "instruction": "What is the AppBar widget in Flutter?",
            "input": "",
            "output": "AppBar is a Material Design app bar that typically appears at the top of a Scaffold. It can contain a title, leading widget (often a menu icon or back button), action buttons, and a flexible space. It supports customization of colors, elevation, and shape, and integrates with the Navigator for automatic back button handling."
        },
        {
            "instruction": "What is the FloatingActionButton in Flutter?",
            "input": "",
            "output": "FloatingActionButton (FAB) is a circular Material Design button that hovers over the content. It is typically used for the primary action on a screen. It is placed in the Scaffold's floatingActionButton property and comes in two sizes: regular and mini. It can also be extended with a label using FloatingActionButton.extended."
        },
        {
            "instruction": "What is the Drawer widget in Flutter?",
            "input": "",
            "output": "Drawer is a Material Design panel that slides in horizontally from the edge of a Scaffold. It is typically used for app navigation. It is accessed via the hamburger menu icon in the AppBar or by swiping from the screen edge. It usually contains a DrawerHeader and a ListView of navigation items like ListTiles."
        },
        {
            "instruction": "What is the Navigator in Flutter?",
            "input": "",
            "output": "Navigator is a widget that manages a stack of Route objects for screen navigation. It works like a stack data structure — you push routes onto it to navigate forward and pop routes to go back. The Navigator.push() and Navigator.pop() methods are commonly used for imperative navigation, while named routes provide declarative navigation."
        },
        {
            "instruction": "What are named routes in Flutter?",
            "input": "",
            "output": "Named routes are a way to define navigation routes as string identifiers in the MaterialApp's routes map. Instead of creating route objects manually, you can navigate using Navigator.pushNamed('/routeName'). They provide a cleaner, more organized approach to navigation but have limitations with passing complex arguments compared to imperative navigation."
        },
        {
            "instruction": "What is the Dart null safety feature?",
            "input": "",
            "output": "Null safety is a feature in Dart that helps prevent null reference errors at compile time. With null safety, types are non-nullable by default — a variable of type String cannot be null. To allow null, you use the nullable type syntax with a question mark (String?). This eliminates an entire class of runtime errors related to null values."
        },
        {
            "instruction": "What are the key Dart data types?",
            "input": "",
            "output": "Dart's key data types include: int and double for numbers (both extend num), String for text, bool for booleans, List for ordered collections, Map for key-value pairs, Set for unique collections, and dynamic/Object for flexible typing. Dart also supports enums, records, and user-defined classes. All types are objects in Dart."
        },
        {
            "instruction": "What is the difference between final and const in Dart?",
            "input": "",
            "output": "Both final and const declare variables that cannot be reassigned. The key difference is: final variables are set at runtime and can only be assigned once, while const variables must be compile-time constants with values determined during compilation. const objects are deeply immutable, meaning their entire object graph is frozen."
        },
        {
            "instruction": "What is async and await in Dart?",
            "input": "",
            "output": "async and await are keywords for handling asynchronous operations in Dart. An async function returns a Future and allows the use of await inside it. await pauses execution of the async function until the Future completes, making asynchronous code look and behave like synchronous code. This simplifies working with network calls, file I/O, and other async operations."
        },
        {
            "instruction": "What is a Future in Dart?",
            "input": "",
            "output": "A Future represents a potential value or error that will be available at some time in the future. It is Dart's way of handling asynchronous operations. A Future can be in one of three states: uncompleted, completed with a value, or completed with an error. You can use await, .then(), or .catchError() to handle Future results."
        },
        {
            "instruction": "What is a Stream in Dart?",
            "input": "",
            "output": "A Stream is a sequence of asynchronous events delivered over time. Unlike a Future which provides a single value, a Stream can emit multiple values. Streams can be single-subscription (listened to once) or broadcast (multiple listeners). They are commonly used for handling continuous data like user input events, WebSocket data, or file reading."
        },
        {
            "instruction": "What are Dart mixins?",
            "input": "",
            "output": "Mixins are a way to reuse code across multiple class hierarchies in Dart. A mixin is defined using the mixin keyword and can be applied to a class using the with keyword. Mixins can contain methods and fields but cannot be instantiated directly. They provide a form of multiple inheritance without the diamond problem."
        },
        {
            "instruction": "What is the purpose of the setState() method in Flutter?",
            "input": "",
            "output": "setState() is a method available in the State class of a StatefulWidget. It notifies the Flutter framework that the internal state has changed and the UI needs to be rebuilt. When called, it triggers a call to the build() method, which reconstructs the widget tree with updated state values. It should only be used for state changes that affect the UI."
        },
        {
            "instruction": "What is the purpose of the dispose() method in Flutter?",
            "input": "",
            "output": "dispose() is a lifecycle method called when a StatefulWidget's State object is permanently removed from the widget tree. It is used to release resources like animation controllers, stream subscriptions, text editing controllers, and focus nodes. Failing to dispose of resources can lead to memory leaks."
        },
        {
            "instruction": "What is the initState() method in Flutter?",
            "input": "",
            "output": "initState() is a lifecycle method called once when a StatefulWidget's State object is first inserted into the widget tree. It is used for one-time initialization tasks such as setting up animation controllers, subscribing to streams, or fetching initial data. It is called before the first build() and should always call super.initState()."
        },
        {
            "instruction": "What is the purpose of the build() method in Flutter?",
            "input": "",
            "output": "The build() method describes the UI of a widget by returning a widget tree. It is called whenever the widget needs to be rendered — on initial creation, when setState() is called, or when parent widgets rebuild. It receives a BuildContext parameter and should be a pure function of the widget's state and configuration without side effects."
        },
        {
            "instruction": "What is the GestureDetector widget in Flutter?",
            "input": "",
            "output": "GestureDetector is a widget that detects various gestures made on its child widget. It can recognize taps, double taps, long presses, drags, and scale gestures. It wraps a child widget and provides callbacks like onTap, onDoubleTap, onLongPress, and onPanUpdate to handle user interactions."
        },
        {
            "instruction": "What is the InkWell widget in Flutter?",
            "input": "",
            "output": "InkWell is a Material Design ripple effect widget that responds to touch events. Unlike GestureDetector, it provides visual feedback through a splash animation when tapped. It is commonly used to wrap non-interactive widgets to make them tappable with Material-style ripple effects. It requires a Material widget ancestor."
        },
        {
            "instruction": "What is the Image widget in Flutter?",
            "input": "",
            "output": "The Image widget displays an image in Flutter. It supports loading images from various sources: Image.asset() for bundled assets, Image.network() for URLs, Image.file() for local files, and Image.memory() for byte data. It provides properties like fit, width, height, and alignment to control how the image is displayed."
        },
        {
            "instruction": "What is the Icon widget in Flutter?",
            "input": "",
            "output": "The Icon widget displays a glyph from an icon font, most commonly from the Material Icons library. It takes an IconData parameter (like Icons.home) and supports customization of size, color, and semantic label. Icons are resolution-independent vector graphics, making them sharp at any size."
        },
        {
            "instruction": "What is the TextField widget in Flutter?",
            "input": "",
            "output": "TextField is a Material Design text input widget that allows users to enter and edit text. It can be customized with decoration (using InputDecoration), keyboard type, text style, and validation. It uses a TextEditingController to read input values and can respond to changes via onChanged, onSubmitted, and other callbacks."
        },
        {
            "instruction": "What is an ElevatedButton in Flutter?",
            "input": "",
            "output": "ElevatedButton is a Material Design button with elevation that responds to touch with an ink splash effect. It replaces the deprecated RaisedButton. It takes an onPressed callback and a child widget (usually Text). When onPressed is null, the button appears disabled. It can be styled using ElevatedButton.styleFrom() or ButtonStyle."
        },
        {
            "instruction": "What is a TextButton in Flutter?",
            "input": "",
            "output": "TextButton is a Material Design button without elevation, typically used for less prominent actions. It replaces the deprecated FlatButton. It displays text (or any widget) and responds to taps with an ink ripple effect. It is commonly used in dialogs, cards, and inline actions where a flat appearance is preferred."
        },
        {
            "instruction": "What is the Flexible widget in Flutter?",
            "input": "",
            "output": "Flexible is a widget that controls how a child of a Row, Column, or Flex fills available space. It has a flex property that determines the proportion of remaining space allocated to it, and a fit property (FlexFit.tight or FlexFit.loose) that controls whether the child must fill all allocated space or can be smaller."
        },
        {
            "instruction": "Explain the concept of keys in Flutter.",
            "input": "",
            "output": "Keys in Flutter are identifiers that help the framework differentiate between widgets of the same type during rebuilds. They are essential when reordering, adding, or removing widgets from a list to preserve state correctly. Types include ValueKey (based on a value), ObjectKey (based on identity), UniqueKey (always unique), and GlobalKey (unique across the entire app)."
        },
        {
            "instruction": "What is the Wrap widget in Flutter?",
            "input": "",
            "output": "Wrap is a layout widget that displays its children in a horizontal or vertical flow, wrapping to the next line when there's no more room on the current line. Unlike Row or Column, Wrap handles overflow gracefully by creating new runs. It accepts spacing and runSpacing parameters to control gaps between children and between runs."
        },
        {
            "instruction": "What is the SingleChildScrollView widget in Flutter?",
            "input": "",
            "output": "SingleChildScrollView is a widget that makes its single child scrollable when the content exceeds the available viewport. Unlike ListView, it renders all content at once (not lazily). It is useful for forms or layouts that might overflow on smaller screens but is not recommended for long lists due to performance concerns."
        },
        {
            "instruction": "What is the SafeArea widget in Flutter?",
            "input": "",
            "output": "SafeArea is a widget that insets its child to avoid intrusions by the operating system, such as the status bar, notch, or navigation bar. It uses MediaQuery to determine the system's padding and applies it to keep content visible and interactive. It is commonly used as a wrapper around the body content of a Scaffold."
        },
        {
            "instruction": "What is the MediaQuery in Flutter?",
            "input": "",
            "output": "MediaQuery is an InheritedWidget that provides information about the current device's screen properties, including size, orientation, padding, text scale factor, and brightness. It is accessed using MediaQuery.of(context) and is essential for building responsive UIs that adapt to different screen sizes and device configurations."
        },
        {
            "instruction": "What is the Opacity widget in Flutter?",
            "input": "",
            "output": "Opacity is a widget that controls the transparency of its child. It takes an opacity value between 0.0 (fully transparent) and 1.0 (fully opaque). While simple to use, it can be expensive because it requires an offscreen buffer. For better performance, prefer using color opacity or FadeTransition for animated opacity changes."
        },
        {
            "instruction": "What is the ClipRRect widget in Flutter?",
            "input": "",
            "output": "ClipRRect is a widget that clips its child using a rounded rectangle. It takes a borderRadius parameter to define the corner rounding. It is commonly used to create rounded corners on images, containers, or other widgets. For simple rectangular clipping, ClipRect can be used instead."
        },
        {
            "instruction": "What is the AspectRatio widget in Flutter?",
            "input": "",
            "output": "AspectRatio is a widget that sizes its child to a specific aspect ratio (width/height). It is useful for maintaining consistent proportions for images, videos, or other content regardless of the parent's constraints. For example, an aspectRatio of 16/9 ensures the child maintains a widescreen ratio."
        },
        {
            "instruction": "What is the Card widget in Flutter?",
            "input": "",
            "output": "Card is a Material Design surface widget that displays content with rounded corners and elevation shadow. It is typically used to present related information in a visually grouped manner. Card supports customization of color, elevation, shape, and margin. It usually wraps a Column or ListTile containing the card's content."
        },
        {
            "instruction": "What is a ListTile widget in Flutter?",
            "input": "",
            "output": "ListTile is a Material Design widget that represents a single fixed-height row with optional leading and trailing widgets, a title, and a subtitle. It is commonly used inside ListView or as children of a Drawer. It provides built-in tap handling via onTap and visual density control, making it ideal for list items and menu options."
        },
        {
            "instruction": "What are packages in Flutter?",
            "input": "",
            "output": "Packages are reusable libraries of Dart code that can be shared across projects. They are distributed through pub.dev, Flutter's package repository. Packages are added to a project by listing them in the pubspec.yaml file under dependencies. They range from UI components and state management solutions to platform-specific plugins for camera, storage, and more."
        },
        {
            "instruction": "What is the difference between a package and a plugin in Flutter?",
            "input": "",
            "output": "A package is a pure Dart library that works across all platforms without native code. A plugin is a specialized type of package that includes platform-specific code (Java/Kotlin for Android, Swift/Objective-C for iOS) to access native device features like camera, GPS, or file system. Plugins use platform channels to communicate between Dart and native code."
        },
        {
            "instruction": "What is pub.dev?",
            "input": "",
            "output": "pub.dev is the official package repository for Dart and Flutter. It hosts thousands of open-source packages and plugins that developers can use in their projects. Each package page shows documentation, version history, example usage, platform compatibility, and a pub points score indicating package quality and maintenance status."
        },
        {
            "instruction": "What is the purpose of the runApp() function in Flutter?",
            "input": "",
            "output": "runApp() is a Flutter framework function that takes a Widget and makes it the root of the widget tree. It inflates the widget and attaches it to the screen, starting the rendering pipeline. It should be called from the main() function and is typically passed a MaterialApp or CupertinoApp widget as the root of the application."
        },
        {
            "instruction": "What is the ThemeData class in Flutter?",
            "input": "",
            "output": "ThemeData defines the visual properties for a Material Design theme in Flutter. It specifies colors, typography, shape themes, and component-level styles that are consistently applied throughout the app. It is set via the theme property of MaterialApp and accessed by descendant widgets using Theme.of(context)."
        },
        {
            "instruction": "What is the Align widget in Flutter?",
            "input": "",
            "output": "Align is a widget that positions its child within itself based on an Alignment value. It can place its child at the center, top-left, bottom-right, or any other position using Alignment coordinates ranging from -1.0 to 1.0 for both x and y axes. FractionalOffset can also be used for 0.0 to 1.0 based positioning."
        },
        {
            "instruction": "What is the Center widget in Flutter?",
            "input": "",
            "output": "Center is a convenience widget that centers its child within the available space. It is actually a special case of the Align widget with alignment set to Alignment.center. It optionally accepts widthFactor and heightFactor parameters that size the Center relative to its child's dimensions rather than expanding to fill all available space."
        },
        {
            "instruction": "What is the FittedBox widget in Flutter?",
            "input": "",
            "output": "FittedBox is a widget that scales and positions its child to fit within the available space according to a specified BoxFit mode. BoxFit options include contain, cover, fill, fitWidth, fitHeight, and scaleDown. It is useful for ensuring content like text or images fits within a constrained area without manual size calculations."
        },
        {
            "instruction": "What is a Future.delayed in Dart?",
            "input": "",
            "output": "Future.delayed creates a Future that completes after a specified Duration. It is commonly used to simulate network delays in testing, create timed operations, or schedule code to run after a delay. For example, Future.delayed(Duration(seconds: 2), () => 'Hello') completes with 'Hello' after a 2-second delay."
        },
        {
            "instruction": "What is the difference between var, final, and const in Dart?",
            "input": "",
            "output": "var declares a mutable variable whose type is inferred from its initial value and can be reassigned. final declares a variable that can only be assigned once at runtime — its value is set when first accessed. const declares a compile-time constant whose value must be determined during compilation. const variables are implicitly final."
        },
        {
            "instruction": "What are Dart generics?",
            "input": "",
            "output": "Generics allow writing type-safe, reusable code in Dart. They let you parameterize classes, functions, and interfaces with type arguments. For example, List<String> ensures a list only contains strings. Generics reduce code duplication while maintaining type safety, and Dart supports generic classes, methods, and type constraints using the extends keyword."
        },
        {
            "instruction": "What is the Dart spread operator?",
            "input": "",
            "output": "The spread operator (...) in Dart unpacks elements from a collection into another collection. For example, [...list1, ...list2] creates a new list combining both lists. The null-aware spread operator (...?) safely handles null collections by not spreading if the value is null. It works with Lists, Sets, and Maps."
        },
        {
            "instruction": "What is the cascade notation (..) in Dart?",
            "input": "",
            "output": "Cascade notation (..) allows performing multiple operations on the same object without repeating the variable name. It returns the original object rather than the method's return value. For example: myList..add(1)..add(2)..add(3) adds three elements to myList in a single expression. It improves code readability for builder-style configurations."
        },
        {
            "instruction": "What is DevTools in Flutter?",
            "input": "",
            "output": "Flutter DevTools is a suite of debugging and performance tools for Flutter applications. It includes a widget inspector for examining the widget tree, a performance view for identifying jank, a memory profiler, a network profiler, a logging view, and a CPU profiler. DevTools can be launched from VS Code, Android Studio, or the command line."
        },
        {
            "instruction": "What is the difference between debug mode, profile mode, and release mode in Flutter?",
            "input": "",
            "output": "Debug mode enables assertions, hot reload, and DevTools but has slower performance. Profile mode compiles to native code with some debugging capability, retaining enough info to profile performance. Release mode is fully optimized for production — it strips debug info, enables tree shaking, and uses AOT compilation for maximum performance."
        },
        {
            "instruction": "What are assertions in Dart?",
            "input": "",
            "output": "Assertions are debugging statements in Dart that check a boolean condition during development. They use the assert() function and are only evaluated in debug mode — they are completely removed in production builds. If the condition is false, an AssertionError is thrown. They are used to catch programming errors early during development."
        },
        {
            "instruction": "What is the purpose of the Divider widget in Flutter?",
            "input": "",
            "output": "Divider is a thin horizontal line widget used to visually separate content in lists and other vertical layouts. It has customizable height (total space occupied), thickness (line thickness), color, and indent/endIndent (margins from edges). VerticalDivider serves the same purpose for horizontal layouts like rows."
        },
        {
            "instruction": "What is the Spacer widget in Flutter?",
            "input": "",
            "output": "Spacer is a widget that creates flexible, empty space within a Row, Column, or Flex. It expands to fill available space, similar to Expanded but without requiring a child widget. It accepts a flex parameter to control how much space it occupies relative to other Spacer or Expanded widgets. It is useful for pushing widgets apart."
        },
        {
            "instruction": "What is the LayoutBuilder widget in Flutter?",
            "input": "",
            "output": "LayoutBuilder is a widget that provides the parent's constraints to its builder function. It rebuilds when the constraints change, making it useful for responsive layouts that adapt based on available space. Unlike MediaQuery which gives screen-level info, LayoutBuilder gives the actual constraints available to that specific widget."
        },
        {
            "instruction": "What is the Visibility widget in Flutter?",
            "input": "",
            "output": "Visibility controls whether a child widget is visible, invisible, or completely removed from the layout. When visible is false and maintainSize is true, the widget is hidden but still occupies space. When maintainSize is false, it is completely removed. It provides a cleaner alternative to conditional rendering with if statements."
        },
        {
            "instruction": "What is the purpose of the late keyword in Dart?",
            "input": "",
            "output": "The late keyword in Dart is used to declare non-nullable variables that are initialized after their declaration. It tells the compiler that the variable will be assigned before it is used, deferring the initialization check to runtime. It is commonly used for variables that depend on initialization logic in initState() or constructors. A LateInitializationError is thrown if accessed before assignment."
        },
        {
            "instruction": "What is a Dart enum?",
            "input": "",
            "output": "An enum (enumeration) in Dart defines a fixed set of named constant values. Starting from Dart 2.17, enhanced enums can have fields, constructors, methods, and can implement interfaces. Enums are used to represent a small, fixed set of options like directions, states, or categories. Each value has an index property starting from 0."
        },
        {
            "instruction": "What is the purpose of the @override annotation in Dart?",
            "input": "",
            "output": "The @override annotation indicates that a method intentionally overrides a superclass method or interface member. While optional, it serves as documentation and helps the analyzer detect errors — if the annotated method does not actually override anything, the analyzer produces a warning. It is a best practice to always use @override."
        },
        {
            "instruction": "What is the CupertinoApp widget in Flutter?",
            "input": "",
            "output": "CupertinoApp is the iOS-style counterpart to MaterialApp. It uses Cupertino (Apple-style) design widgets and themes. It provides iOS-native look and feel including navigation transitions, tab bars, and controls. While MaterialApp can be used on iOS, CupertinoApp is preferred when building apps that should closely match iOS design guidelines."
        },
        {
            "instruction": "What is the BottomNavigationBar widget in Flutter?",
            "input": "",
            "output": "BottomNavigationBar is a Material Design widget that displays navigation items at the bottom of the screen. It takes a list of BottomNavigationBarItem widgets and provides currentIndex and onTap properties for navigation handling. It supports fixed and shifting display types, and is placed in the Scaffold's bottomNavigationBar property."
        },
        {
            "instruction": "What is the TabBar widget in Flutter?",
            "input": "",
            "output": "TabBar is a Material Design widget that displays a row of tabs, typically used with a TabBarView to create tabbed navigation. It requires a TabController to synchronize tab selection with content. DefaultTabController can be used as a simpler alternative that automatically creates the controller. Each tab can display text, icons, or both."
        },
        {
            "instruction": "What is the CircularProgressIndicator in Flutter?",
            "input": "",
            "output": "CircularProgressIndicator is a Material Design widget that shows progress as a spinning circle. It can be determinate (showing specific progress from 0.0 to 1.0 via the value property) or indeterminate (continuously spinning when value is null). It is commonly used as a loading indicator during async operations."
        },
        {
            "instruction": "What is the SnackBar widget in Flutter?",
            "input": "",
            "output": "SnackBar is a Material Design widget that displays a brief message at the bottom of the screen. It is shown using ScaffoldMessenger.of(context).showSnackBar(). It supports customization of content, duration, action button, and behavior (fixed or floating). SnackBars are used for lightweight feedback like confirming an action or showing errors."
        },
        {
            "instruction": "What is the AlertDialog widget in Flutter?",
            "input": "",
            "output": "AlertDialog is a Material Design dialog widget that interrupts the user to inform them about a situation or request confirmation. It is displayed using showDialog(). It contains a title, content area, and action buttons. It can be dismissed by tapping outside (if barrierDismissible is true) or by pressing the back button."
        },
        {
            "instruction": "What is the showDialog function in Flutter?",
            "input": "",
            "output": "showDialog is a function that displays a Material Design dialog above the current content. It takes a BuildContext and a builder function that returns the dialog widget. It returns a Future that resolves when the dialog is dismissed. The dialog is displayed as a modal overlay with an optional barrier color behind it."
        },
        {
            "instruction": "What is the Chip widget in Flutter?",
            "input": "",
            "output": "Chip is a compact Material Design element that represents an attribute, action, or filter. Flutter provides several variants: Chip (basic), ActionChip (for actions), FilterChip (for filtering), ChoiceChip (for single selection), and InputChip (for user input like tags). They can display a label, avatar, delete icon, and respond to interactions."
        },
        {
            "instruction": "What is the Tooltip widget in Flutter?",
            "input": "",
            "output": "Tooltip is a Material Design widget that displays a text message when the user long-presses or hovers over a widget. It is used to provide additional context or describe an element's function. Many Material widgets like IconButton already have a built-in tooltip property. Custom tooltips can wrap any widget."
        },
        {
            "instruction": "What is the Stepper widget in Flutter?",
            "input": "",
            "output": "Stepper is a Material Design widget that displays a series of steps in a vertical or horizontal layout. Each step has a title, content, and state (indexed, editing, complete, disabled, error). The Stepper manages step navigation with onStepContinue, onStepCancel, and onStepTapped callbacks, making it useful for multi-step forms and wizards."
        },
        {
            "instruction": "What is the AnimatedContainer widget in Flutter?",
            "input": "",
            "output": "AnimatedContainer is an implicitly animated version of the Container widget. When its properties change (size, color, padding, margin, decoration, etc.), it automatically animates the transition over a specified duration with an optional curve. It simplifies animations by eliminating the need for explicit animation controllers for simple property changes."
        },
        {
            "instruction": "What is the difference between Cupertino and Material design in Flutter?",
            "input": "",
            "output": "Material Design is Google's design system with bold colors, elevation shadows, and ripple effects — used with MaterialApp and Material widgets. Cupertino is Apple's iOS design system with translucent surfaces, iOS-style navigation, and subtle animations — used with CupertinoApp and Cupertino widgets. Flutter supports both, and many apps use Material for both platforms."
        },
        {
            "instruction": "What is the purpose of the const constructor in Flutter widgets?",
            "input": "",
            "output": "A const constructor creates compile-time constant widgets, meaning the same widget instance is reused across rebuilds. This improves performance because Flutter can skip rebuilding const widgets since they never change. Using const with widgets like Text, Icon, Padding, and SizedBox is a recommended optimization practice."
        },
        {
            "instruction": "What is the Selector widget pattern?",
            "input": "",
            "output": "While not a built-in Flutter widget, Selector is a widget from the Provider package that rebuilds only when a selected value from the provided object changes. Unlike Consumer which rebuilds on any change, Selector extracts a specific value and only triggers rebuilds when that value differs. This optimizes performance in complex UIs."
        },
        # ─── Additional Basic Questions ─────────────────────────────
        {
            "instruction": "What is the Flutter SDK?",
            "input": "",
            "output": "The Flutter SDK is a complete software development kit that includes the Flutter framework, Dart SDK, development tools, and command-line utilities. It provides the flutter command for creating projects, running apps, building releases, and managing dependencies. The SDK also includes the Flutter engine (written in C++) that handles rendering, platform interaction, and Dart runtime."
        },
        {
            "instruction": "How do you create a new Flutter project?",
            "input": "",
            "output": "A new Flutter project is created using the command 'flutter create project_name' in the terminal. This generates a complete project structure with lib/main.dart as the entry point, platform-specific directories (android/, ios/), pubspec.yaml for dependencies, and test/ for unit tests. You can also specify the organization, platform, and template using additional flags."
        },
        {
            "instruction": "What is the lib folder in a Flutter project?",
            "input": "",
            "output": "The lib folder is the main directory for all Dart source code in a Flutter project. It contains main.dart as the app entry point and all other Dart files organized into subdirectories. Only code within the lib folder is compiled into the final application. It is common to organize this folder into subfolders like screens/, widgets/, models/, services/, and utils/."
        },
        {
            "instruction": "What is the android folder in a Flutter project?",
            "input": "",
            "output": "The android folder contains the native Android project configuration and code. It includes the AndroidManifest.xml for app permissions and metadata, build.gradle files for build configuration, and the MainActivity class. Developers modify this folder to configure Android-specific settings like app icons, splash screens, permissions, and native platform channel implementations."
        },
        {
            "instruction": "What is the ios folder in a Flutter project?",
            "input": "",
            "output": "The ios folder contains the native iOS project files, including the Xcode workspace. It has the Info.plist for app configuration, AppDelegate for native iOS lifecycle handling, and Podfile for CocoaPods dependencies. Developers modify this folder for iOS-specific settings like app icons, launch screens, entitlements, and native code for platform channels."
        },
        {
            "instruction": "What is the test folder in a Flutter project?",
            "input": "",
            "output": "The test folder contains unit tests and widget tests for the Flutter application. Test files are named with the _test.dart suffix and use the flutter_test package. Tests can be run using 'flutter test' from the command line. This folder mirrors the lib folder structure and contains test files corresponding to the source files being tested."
        },
        {
            "instruction": "What is the web folder in a Flutter project?",
            "input": "",
            "output": "The web folder contains files needed for Flutter web deployment, including index.html as the entry point, favicon.ico, manifest.json for PWA configuration, and the icons folder. Flutter compiles Dart code to JavaScript and renders the UI using either HTML/CSS/Canvas or CanvasKit (WebAssembly + Skia). The web folder is created when web support is enabled."
        },
        {
            "instruction": "What is the difference between Flutter and native development?",
            "input": "",
            "output": "Native development uses platform-specific languages (Kotlin/Java for Android, Swift/Objective-C for iOS) with separate codebases for each platform. Flutter uses a single Dart codebase for all platforms and renders UI with its own engine. Native offers deeper platform integration, while Flutter provides faster development, consistent UI, and lower maintenance cost for cross-platform apps."
        },
        {
            "instruction": "What is the Flutter engine?",
            "input": "",
            "output": "The Flutter engine is the core runtime written in C++ that powers Flutter applications. It provides low-level rendering using Skia (or Impeller), text layout, file and network I/O, accessibility support, plugin architecture, and the Dart runtime. The engine communicates with platform-specific embedders that handle windowing, input, and platform API access."
        },
        {
            "instruction": "What is the difference between runApp() and void main()?",
            "input": "",
            "output": "void main() is the standard Dart entry point function that gets called when the app starts. runApp() is a Flutter-specific function called inside main() that takes a widget and attaches it as the root of the widget tree to the screen. main() can contain initialization code before runApp(), such as WidgetsFlutterBinding.ensureInitialized() for plugin setup."
        },
        {
            "instruction": "What is WidgetsFlutterBinding.ensureInitialized()?",
            "input": "",
            "output": "WidgetsFlutterBinding.ensureInitialized() initializes the binding between the Flutter framework and the Flutter engine before runApp() is called. It is required when you need to call native code or use plugins before the app starts, such as initializing Firebase, reading SharedPreferences, or setting preferred orientations. Without it, plugin calls before runApp() will crash."
        },
        {
            "instruction": "What is the Scaffold's body property?",
            "input": "",
            "output": "The body property of Scaffold is where the main content of the screen is placed. It accepts any widget and displays it in the area below the AppBar and above the BottomNavigationBar. The body content is typically wrapped in widgets like SingleChildScrollView, ListView, or Column. It occupies the remaining space after the AppBar and bottom widgets are laid out."
        },
        {
            "instruction": "What is the difference between Scaffold and SafeArea?",
            "input": "",
            "output": "Scaffold provides the basic Material Design structure with slots for AppBar, body, drawer, FAB, and bottom navigation. SafeArea is a widget that insets its child to avoid system UI intrusions like the status bar, notch, and navigation bar. They serve different purposes but are commonly used together — SafeArea is often wrapped around Scaffold's body content."
        },
        {
            "instruction": "What is the Wrap widget used for?",
            "input": "",
            "output": "The Wrap widget displays its children in a horizontal or vertical flow and automatically wraps to the next line when there is no remaining space on the current line. It is commonly used for displaying tags, chips, or badges that need to flow naturally. It accepts spacing and runSpacing parameters for controlling gaps between items and lines."
        },
        {
            "instruction": "What is the RichText widget in Flutter?",
            "input": "",
            "output": "RichText is a widget that displays text with multiple styles within a single paragraph. It takes a TextSpan tree where each span can have its own TextStyle, gesture recognizers, and child spans. This allows mixing bold, italic, colored, and linked text in one block. The simpler Text.rich() constructor provides a more convenient API for the same functionality."
        },
        {
            "instruction": "What is a TextSpan in Flutter?",
            "input": "",
            "output": "TextSpan is an immutable span of styled text used with RichText or Text.rich(). It has a text property for the string, a style property for TextStyle, a children property for nested spans, and a recognizer property for gesture detection like tap. TextSpans form a tree structure allowing complex text formatting within a single text block."
        },
        {
            "instruction": "What is the SelectableText widget in Flutter?",
            "input": "",
            "output": "SelectableText is a widget that displays text that users can select and copy. Unlike the regular Text widget which doesn't support selection, SelectableText allows long-press to select text and provides a toolbar for copy operations. It supports the same styling as Text via TextStyle and can also display rich text with SelectableText.rich()."
        },
        {
            "instruction": "What is the Placeholder widget in Flutter?",
            "input": "",
            "output": "Placeholder is a widget that draws a box with an X pattern to indicate that a widget is not yet implemented. It is useful during development as a visual placeholder for future UI components. It takes optional fallbackWidth and fallbackHeight parameters and uses a customizable strokeWidth and color for the X pattern."
        },
        {
            "instruction": "What is the CircleAvatar widget in Flutter?",
            "input": "",
            "output": "CircleAvatar is a widget that displays a circular image or initials representing a user or entity. It supports background images via backgroundImage, text content via child, background and foreground colors, and radius customization. It is commonly used in user profile displays, contact lists, and as leading widgets in ListTile."
        },
        {
            "instruction": "What is the Switch widget in Flutter?",
            "input": "",
            "output": "Switch is a Material Design toggle widget that allows users to switch between on and off states. It has a value property for the current state and an onChanged callback for handling state changes. Switch.adaptive renders a CupertinoSwitch on iOS and a Material Switch on Android for platform-appropriate appearance."
        },
        {
            "instruction": "What is the Checkbox widget in Flutter?",
            "input": "",
            "output": "Checkbox is a Material Design widget that allows users to select or deselect an option. It has a value (bool or null for tristate), an onChanged callback, and customizable colors. CheckboxListTile combines a Checkbox with a ListTile for labeled checkboxes. The tristate property enables a third indeterminate state."
        },
        {
            "instruction": "What is the Radio widget in Flutter?",
            "input": "",
            "output": "Radio is a Material Design widget for selecting one option from a group. Each Radio has a value and groupValue — when they match, the radio is selected. The onChanged callback updates the group value. RadioListTile provides a convenient labeled version. Only one Radio in a group can be selected at a time."
        },
        {
            "instruction": "What is the Slider widget in Flutter?",
            "input": "",
            "output": "Slider is a Material Design widget that lets users select a value from a continuous or discrete range by dragging a thumb. It has min, max, value, and onChanged properties. The divisions property creates discrete steps. RangeSlider allows selecting a range with two thumbs. Labels and active/inactive colors are customizable."
        },
        {
            "instruction": "What is the DropdownButton widget in Flutter?",
            "input": "",
            "output": "DropdownButton displays a button that opens a dropdown menu with selectable items. It takes a list of DropdownMenuItem widgets, a value for the current selection, and an onChanged callback. DropdownButtonFormField integrates with Form validation. The menu appears as an overlay below or above the button depending on available space."
        },
        {
            "instruction": "What is the DatePicker in Flutter?",
            "input": "",
            "output": "Flutter provides showDatePicker() function that displays a Material Design date picker dialog. It takes initialDate, firstDate, lastDate parameters and returns a Future<DateTime?>. The date picker supports calendar and input modes. showDateRangePicker() allows selecting a date range. For iOS-style, CupertinoDatePicker is available."
        },
        {
            "instruction": "What is the TimePicker in Flutter?",
            "input": "",
            "output": "Flutter provides showTimePicker() function that displays a Material Design time picker dialog. It takes an initialTime parameter and returns a Future<TimeOfDay?>. The picker supports dial and input entry modes. For 24-hour format, use the builder parameter with MediaQuery to override alwaysUse24HourFormat."
        },
        {
            "instruction": "What is the Drawer's endDrawer property?",
            "input": "",
            "output": "Scaffold supports two drawers: drawer (slides from the left/start) and endDrawer (slides from the right/end). Both work identically but appear from opposite sides. The endDrawer is opened via Scaffold.of(context).openEndDrawer() or by swiping from the right edge. It is commonly used for filters, settings, or secondary navigation."
        },
        {
            "instruction": "What is the WillPopScope replacement in newer Flutter?",
            "input": "",
            "output": "In Flutter 3.12 and later, WillPopScope was deprecated in favor of PopScope. PopScope uses a canPop property (boolean) and an onPopInvokedWithResult callback instead of the Future-based onWillPop. This provides clearer semantics and better integration with the new navigation APIs. The canPop value directly controls whether back navigation is allowed."
        },
        {
            "instruction": "What is the BackdropFilter widget in Flutter?",
            "input": "",
            "output": "BackdropFilter applies a filter effect to the area behind its child widget, not to the child itself. It is commonly used with ImageFilter.blur() to create frosted glass effects or blurred backgrounds. It must be placed inside a Stack behind its siblings to affect the content beneath it. The filter area is defined by the clip of the parent."
        },
        {
            "instruction": "What is the ShaderMask widget in Flutter?",
            "input": "",
            "output": "ShaderMask applies a shader (gradient, image, etc.) as a mask to its child widget. It takes a shaderCallback that receives the bounds and returns a Shader, and a blendMode that controls how the shader is combined with the child. It is commonly used for gradient text effects, fading edges, and creative visual effects."
        },
        {
            "instruction": "What is the PhysicalModel widget in Flutter?",
            "input": "",
            "output": "PhysicalModel creates a layer with a physical shape that casts a shadow. Unlike Container with BoxDecoration, PhysicalModel renders elevation shadows using the rendering engine for better performance. It supports customizable color, elevation, shadow color, and shape (rectangle or circle). It is useful for creating card-like surfaces without Material widget overhead."
        },
        {
            "instruction": "What is the difference between double.infinity and double.maxFinite?",
            "input": "",
            "output": "double.infinity represents positive infinity and is commonly used with width or height to make a widget expand to fill all available space. double.maxFinite is the largest finite double value. In Flutter layout, double.infinity tells the framework the widget wants to be as large as possible within its constraints, while maxFinite is rarely used in layout."
        },
        {
            "instruction": "What is the difference between EdgeInsets and EdgeInsetsDirectional?",
            "input": "",
            "output": "EdgeInsets uses physical directions (left, top, right, bottom) that don't change with text direction. EdgeInsetsDirectional uses logical directions (start, top, end, bottom) that automatically flip based on the text direction (LTR or RTL). Use EdgeInsetsDirectional for internationalized apps that need to support right-to-left languages like Arabic and Hebrew."
        },
        {
            "instruction": "What is the Dart extension type?",
            "input": "",
            "output": "Extension types, introduced in Dart 3.3, provide a zero-cost wrapper around an existing type. Unlike extension methods, extension types create a new static type that hides the underlying type's interface. They are compiled away at runtime (no allocation overhead), making them useful for type-safe wrappers around IDs, units, and API types without runtime cost."
        },
        {
            "instruction": "What are abstract classes in Dart?",
            "input": "",
            "output": "Abstract classes in Dart cannot be instantiated directly and are declared with the abstract keyword. They can contain both abstract methods (without implementation) and concrete methods. Subclasses must implement all abstract methods. Abstract classes define interfaces and shared behavior. In Dart 3.0+, use interface class instead when only defining a contract."
        },
        {
            "instruction": "What is the difference between implements and extends in Dart?",
            "input": "",
            "output": "extends creates a subclass that inherits implementation from a superclass — you can override methods but also use inherited ones. implements treats the class as an interface — you must provide implementations for ALL members, inheriting nothing. A class can extend only one class but implement multiple interfaces. Use extends for is-a relationships and implements for contracts."
        },
        {
            "instruction": "What is the Dart Map data type?",
            "input": "",
            "output": "Map in Dart is a collection of key-value pairs where each key is unique. It is declared as Map<KeyType, ValueType> and created with literals {key: value} or the Map constructor. Common operations include map[key] for access, map[key] = value for insertion, containsKey(), remove(), forEach(), and entries. Keys must have consistent hashCode and == implementations."
        },
        {
            "instruction": "What is the Dart Set data type?",
            "input": "",
            "output": "Set in Dart is an unordered collection of unique elements. It is declared as Set<Type> and created with literals {element} or the Set constructor. Adding duplicate elements has no effect. Common operations include add(), remove(), contains(), union(), intersection(), and difference(). Sets are useful when you need to ensure uniqueness and fast lookup."
        },
        {
            "instruction": "What is the Dart List data type?",
            "input": "",
            "output": "List in Dart is an ordered collection of elements accessible by index. It is declared as List<Type> and created with literals [element] or the List constructor. Lists can be fixed-length or growable. Common operations include add(), remove(), insert(), sort(), map(), where(), and fold(). List indexing is zero-based."
        },
        {
            "instruction": "What are named parameters in Dart?",
            "input": "",
            "output": "Named parameters in Dart are wrapped in curly braces and are optional by default. They are specified by name when calling: function(name: value). They can be made mandatory with the required keyword. Named parameters improve readability for functions with many parameters and allow specifying only the parameters you need, in any order."
        },
        {
            "instruction": "What are positional parameters in Dart?",
            "input": "",
            "output": "Positional parameters in Dart are specified by their position in the argument list. Required positional parameters are listed without brackets. Optional positional parameters are wrapped in square brackets [] and can have default values. They must be provided in order when calling the function. Positional parameters are concise but less readable for many arguments."
        },
        {
            "instruction": "What is string interpolation in Dart?",
            "input": "",
            "output": "String interpolation in Dart allows embedding expressions inside string literals using the $ symbol. Simple variables use $variable and complex expressions use ${expression}. For example, 'Hello $name, you are ${age + 1} years old'. This is more readable and efficient than string concatenation with the + operator."
        },
        {
            "instruction": "What is the ternary operator in Dart?",
            "input": "",
            "output": "The ternary operator in Dart is a concise conditional expression: condition ? valueIfTrue : valueIfFalse. It evaluates the condition and returns one of two values. It is commonly used in Flutter's build method for conditional UI: Text(isLoggedIn ? 'Welcome' : 'Please log in'). It should be used for simple conditions; complex logic should use if-else."
        },
        {
            "instruction": "What is the null-aware operator (?.) in Dart?",
            "input": "",
            "output": "The null-aware operator (?.) in Dart safely accesses members of an object that might be null. If the object is null, the expression returns null instead of throwing a NoSuchMethodError. For example, user?.name returns null if user is null. It can be chained: user?.address?.city. The ?? operator provides a default: user?.name ?? 'Unknown'."
        },
        {
            "instruction": "What is the null coalescing operator (??) in Dart?",
            "input": "",
            "output": "The null coalescing operator (??) returns the left operand if it's not null, otherwise returns the right operand. For example, name ?? 'Default' returns name if it's not null, else 'Default'. The ??= operator assigns a value only if the variable is currently null: name ??= 'Default'. These operators simplify null handling code."
        },
        {
            "instruction": "What is the bang operator (!) in Dart?",
            "input": "",
            "output": "The bang operator (!) in Dart asserts that a nullable value is not null. For example, String? name = getName(); print(name!.length) tells the compiler that name is guaranteed to be non-null. If the value is actually null at runtime, it throws a TypeError. Use it sparingly and only when you are certain the value is non-null."
        },
        {
            "instruction": "What is the difference between is and as in Dart?",
            "input": "",
            "output": "The is operator checks if an object is of a specific type and returns a boolean: if (obj is String). Dart automatically smart-casts after is checks. The as operator explicitly casts an object to a type: (obj as String).length. If the cast fails, as throws a CastError. Use is for safe type checking and as for explicit casting."
        },
        {
            "instruction": "What are closures in Dart?",
            "input": "",
            "output": "Closures in Dart are functions that capture variables from their enclosing scope. A closure retains access to these variables even after the enclosing function has returned. For example, a function returning another function that uses a local variable creates a closure. Closures are fundamental to callbacks, event handlers, and functional programming patterns in Dart."
        },
        {
            "instruction": "What is the for-in loop in Dart?",
            "input": "",
            "output": "The for-in loop iterates over elements of an Iterable (List, Set, Map entries, etc.). Syntax: for (var item in collection) { ... }. It is cleaner than index-based for loops when you don't need the index. For Maps, iterate over map.entries to access both keys and values: for (var entry in map.entries) { entry.key; entry.value; }."
        },
        {
            "instruction": "What is the collection if and collection for in Dart?",
            "input": "",
            "output": "Collection if and collection for are Dart features that allow conditional and iterative element creation inside collection literals. Collection if: [1, 2, if (addThree) 3]. Collection for: [for (var i in items) Text(i)]. These are especially useful in Flutter for conditionally including widgets in a list without separate builder logic."
        },
        {
            "instruction": "How do you handle exceptions in Dart?",
            "input": "",
            "output": "Dart uses try-catch-finally for exception handling. try wraps code that may throw, catch handles exceptions (optionally specifying the type: on FormatException catch(e)), and finally runs cleanup code regardless of outcome. Dart has two types of throwable objects: Exception (recoverable) and Error (programming mistakes). Custom exceptions extend Exception."
        },
        {
            "instruction": "What is a Dart isolate vs a thread?",
            "input": "",
            "output": "Dart isolates are independent memory spaces that don't share state, communicating only via message passing through SendPort and ReceivePort. Traditional threads share memory and require synchronization primitives like locks and mutexes. Isolates avoid race conditions and deadlocks by design but have higher overhead for sharing data since all data must be serialized between isolates."
        },
        {
            "instruction": "What is the Iterable class in Dart?",
            "input": "",
            "output": "Iterable is the base class for collections that can be iterated. List and Set both extend Iterable. It provides lazy evaluation methods like map(), where(), expand(), take(), skip(), and fold() that don't create new collections until iterated. Using Iterable methods creates efficient processing pipelines. Convert to List with .toList() when needed."
        },
        {
            "instruction": "What is the difference between synchronous and asynchronous generators in Dart?",
            "input": "",
            "output": "Synchronous generators (sync*) produce values lazily using yield and return an Iterable. Asynchronous generators (async*) produce values over time using yield and return a Stream. sync* is used for lazy collection computation, while async* is used for emitting events like WebSocket messages, timer ticks, or database query results over time."
        },
        {
            "instruction": "What is the Dart type system?",
            "input": "",
            "output": "Dart has a sound type system with strong static typing and type inference. It supports generics, nullable types (?), type aliases (typedef), sealed classes, and extension types. The type system is sound — if a variable has type T, it will always hold a value of type T at runtime. Type inference via var, final, and const reduces boilerplate."
        },
        {
            "instruction": "What is the purpose of the assert keyword in Dart?",
            "input": "",
            "output": "assert evaluates a boolean expression during development and throws an AssertionError if it's false. Assertions are completely removed in production builds, making them zero-cost in release mode. They are used to catch programming errors early: assert(value >= 0, 'Value must be non-negative'). Flutter framework uses assertions extensively for parameter validation."
        },
        {
            "instruction": "What is the difference between print() and debugPrint() in Flutter?",
            "input": "",
            "output": "print() outputs text to the console but can lose output when printing rapidly because the system logger buffer fills up. debugPrint() throttles output to prevent dropped messages, ensuring all logs are visible. debugPrint() is recommended for Flutter debugging. Both are removed from release builds, but log() from dart:developer persists in profile mode."
        },
        {
            "instruction": "What is the BoxDecoration class in Flutter?",
            "input": "",
            "output": "BoxDecoration is a class that defines the visual decoration of a Container or DecoratedBox. It supports background color, gradient, image, border, borderRadius, shape, and boxShadow. Multiple BoxDecoration properties can be combined for complex visual effects. It is applied through the decoration property and cannot be used simultaneously with the color property."
        },
        {
            "instruction": "What is the LinearGradient class in Flutter?",
            "input": "",
            "output": "LinearGradient creates a gradient that transitions linearly between colors along a line defined by begin and end alignment points. It takes a list of colors and optional stops to control transition positions. It is used in BoxDecoration for backgrounds, ShaderMask for text effects, and Container decoration. It extends the Gradient class."
        },
        {
            "instruction": "What is the RadialGradient class in Flutter?",
            "input": "",
            "output": "RadialGradient creates a circular gradient that radiates outward from a center point. It takes center, radius, colors, and stops parameters. The gradient transitions from the center color outward through the list of colors. It is used in BoxDecoration and ShaderMask for creating spotlight effects, glows, and circular color transitions."
        },
        {
            "instruction": "What is the DecoratedBox widget in Flutter?",
            "input": "",
            "output": "DecoratedBox is a widget that paints a Decoration (typically BoxDecoration) before or after its child. It is the underlying widget that Container uses for decoration. The position property controls whether decoration is painted behind (background) or in front of (foreground) the child. It is more efficient than Container when only decoration is needed."
        },
        {
            "instruction": "What is the DefaultTextStyle widget in Flutter?",
            "input": "",
            "output": "DefaultTextStyle is an InheritedWidget that sets the default TextStyle for all descendant Text widgets. Any Text widget without an explicit style inherits the nearest DefaultTextStyle. It is how MaterialApp and Scaffold themes propagate text styling through the widget tree. It can be overridden locally by wrapping a subtree in a new DefaultTextStyle."
        },
        {
            "instruction": "What is the IconTheme widget in Flutter?",
            "input": "",
            "output": "IconTheme is an InheritedWidget that provides default IconThemeData (color, size, opacity) to all descendant Icon widgets. Like DefaultTextStyle for text, it allows setting icon styling at a subtree level. MaterialApp theme's iconTheme automatically provides a default. IconTheme.of(context) retrieves the current icon theme in build methods."
        },
        {
            "instruction": "What is the ButtonStyle class in Flutter?",
            "input": "",
            "output": "ButtonStyle defines the visual appearance of Material buttons (ElevatedButton, TextButton, OutlinedButton). It uses MaterialStateProperty for state-dependent styling (pressed, hovered, disabled). Properties include backgroundColor, foregroundColor, elevation, shape, padding, and textStyle. The styleFrom() factory on each button class provides a simpler API for common customizations."
        },
        {
            "instruction": "What is the InputDecoration class in Flutter?",
            "input": "",
            "output": "InputDecoration defines the visual appearance of a TextField or TextFormField. It provides labelText, hintText, helperText, errorText, prefixIcon, suffixIcon, border, filled, and content padding properties. InputDecorationTheme in ThemeData sets default decoration for all text fields. The border can be OutlineInputBorder, UnderlineInputBorder, or InputBorder.none."
        },
        {
            "instruction": "What is the OutlineInputBorder in Flutter?",
            "input": "",
            "output": "OutlineInputBorder creates a rectangular border around a TextField with rounded corners. It is set via InputDecoration's border property. It takes borderRadius and borderSide parameters. Three states are customizable: border (default), focusedBorder (when focused), and errorBorder (when validation fails). It is the most commonly used border style for modern form designs."
        },
        {
            "instruction": "What is the ColorScheme class in Flutter?",
            "input": "",
            "output": "ColorScheme is a set of 30+ colors that define a Material 3 color theme. It replaces the older primarySwatch approach. Key colors include primary, secondary, tertiary, surface, background, error, and their on-variants (onPrimary, etc.). ColorScheme.fromSeed() generates a harmonious scheme from a single seed color. It is set in ThemeData.colorScheme."
        },
        {
            "instruction": "What is Material 3 in Flutter?",
            "input": "",
            "output": "Material 3 (Material You) is the latest version of Google's Material Design system. Flutter adopted Material 3 as the default starting from Flutter 3.16. It features dynamic color schemes generated from a seed color, updated component designs with rounded shapes, new typography scale, and adaptive density. Enable/disable with ThemeData(useMaterial3: true/false)."
        },
        {
            "instruction": "What is the difference between TextTheme and Typography in Flutter?",
            "input": "",
            "output": "TextTheme is a collection of named TextStyles (displayLarge, headlineMedium, bodySmall, etc.) that define the text styling throughout the app. Typography defines the base font geometry for Material Design. TextTheme is customized per-app, while Typography provides platform-specific defaults (tall, dense, english). ThemeData.textTheme overrides the default TextTheme."
        },
        {
            "instruction": "What is the Flexible vs Expanded difference in Flutter?",
            "input": "",
            "output": "Both are used in Row/Column/Flex, but they differ in fit behavior. Expanded (FlexFit.tight) forces its child to fill all the space allocated by the flex factor. Flexible (default FlexFit.loose) allows its child to be smaller than the allocated space. Use Expanded when the child must fill space, Flexible when the child should have a maximum but can be smaller."
        },
        {
            "instruction": "What is the Material widget in Flutter?",
            "input": "",
            "output": "Material is a foundational widget that provides a surface following Material Design specifications. It clips content, applies elevation shadows, animates shape and color changes, and enables ink splash effects. Widgets like InkWell require a Material ancestor to render ripple effects. Scaffold automatically provides a Material surface for its body content."
        },
        {
            "instruction": "What is the difference between margin and padding in Flutter?",
            "input": "",
            "output": "Padding creates empty space inside a widget's bounds, between the widget's border and its child. Margin creates empty space outside the widget's bounds, between the widget and its siblings. In Flutter, padding is set via the Padding widget or Container's padding property. Margins are set via Container's margin property, which is implemented using Padding around the Container."
        },
        {
            "instruction": "What is the ResizeImage class in Flutter?",
            "input": "",
            "output": "ResizeImage is an ImageProvider that resizes an image before decoding it into memory. By specifying target width and/or height, it reduces memory usage for large images that are displayed at smaller sizes. It wraps another ImageProvider: ResizeImage(AssetImage('photo.jpg'), width: 200). This is more efficient than using Image widget's fit property alone."
        },
        {
            "instruction": "What is the precacheImage function in Flutter?",
            "input": "",
            "output": "precacheImage() pre-loads an image into the image cache before it is needed by an Image widget. This prevents visible loading delays when the widget first builds. It returns a Future that completes when the image is cached. It is typically called in initState() or didChangeDependencies() with the BuildContext: precacheImage(AssetImage('bg.png'), context)."
        },
        {
            "instruction": "What is the ScrollController in Flutter?",
            "input": "",
            "output": "ScrollController controls and monitors a scrollable widget's scroll position. It provides offset, animateTo(), jumpTo(), and addListener() for scroll events. It can be passed to ListView, GridView, or CustomScrollView via the controller property. It must be disposed in dispose() and is useful for scroll-to-top buttons, infinite scroll pagination, and parallax effects."
        },
        {
            "instruction": "What is the NotificationListener widget in Flutter?",
            "input": "",
            "output": "NotificationListener is a widget that listens for notifications bubbling up from child widgets. It takes a type parameter specifying which notification type to catch (e.g., ScrollNotification, SizeChangedLayoutNotification). Its onNotification callback receives the notification and returns a bool — true to stop the notification from continuing up the tree, false to let it propagate."
        },
        {
            "instruction": "What is the flutter doctor command?",
            "input": "",
            "output": "flutter doctor is a CLI command that checks the Flutter development environment and reports the status of required tools and configurations. It verifies the Flutter SDK, Dart SDK, Android toolchain (Android Studio, SDK, licenses), iOS toolchain (Xcode, CocoaPods), connected devices, and IDE plugins. It helps diagnose setup issues with clear instructions for fixes."
        },
        {
            "instruction": "What is the flutter pub get command?",
            "input": "",
            "output": "flutter pub get downloads and installs all dependencies listed in pubspec.yaml. It resolves version constraints, downloads packages from pub.dev, and generates the pubspec.lock file that pins exact versions. It also generates the .dart_tool/package_config.json file for the Dart analyzer. It is automatically run when creating a project or adding new dependencies."
        },
        {
            "instruction": "What is the flutter build command?",
            "input": "",
            "output": "flutter build compiles the Flutter app for production release. Common variants: flutter build apk (Android APK), flutter build appbundle (Android App Bundle for Play Store), flutter build ipa (iOS), flutter build web (web deployment). It uses AOT compilation, tree shaking, and code minification for optimal size and performance."
        },
        {
            "instruction": "What is the flutter analyze command?",
            "input": "",
            "output": "flutter analyze runs Dart static analysis on the project code following rules defined in analysis_options.yaml. It checks for type errors, unused imports, deprecated APIs, code style violations, and potential bugs. It returns exit code 0 if no issues are found. It is commonly used in CI/CD pipelines to enforce code quality."
        },
        {
            "instruction": "What is the flutter clean command?",
            "input": "",
            "output": "flutter clean removes the build directory and all generated files (build/, .dart_tool/, .flutter-plugins, .flutter-plugins-dependencies). It is used to resolve build issues caused by corrupted caches, stale build artifacts, or dependency conflicts. After flutter clean, run flutter pub get to restore dependencies before building again."
        },
        {
            "instruction": "What is the Ticker class in Flutter?",
            "input": "",
            "output": "Ticker calls a callback function once per animation frame (typically 60 times per second). It is used by AnimationController to drive animations. The TickerProvider mixin (via SingleTickerProviderStateMixin or TickerProviderStateMixin) creates Tickers that are automatically muted when the widget is not visible, preventing unnecessary work for off-screen animations."
        },
        {
            "instruction": "What is the AbsorbPointer widget in Flutter?",
            "input": "",
            "output": "AbsorbPointer prevents its child's subtree from receiving pointer events (taps, drags, etc.) when its absorbing property is true. Unlike IgnorePointer which lets events pass through to widgets behind it, AbsorbPointer stops events entirely — neither the child nor the widgets beneath it receive the event. It is useful for disabling interaction during loading states."
        },
        {
            "instruction": "What is the IgnorePointer widget in Flutter?",
            "input": "",
            "output": "IgnorePointer makes its child invisible to hit testing, allowing pointer events to pass through to widgets beneath it in the Stack. When ignoring is true, taps on the child are received by whatever widget is behind it. Unlike AbsorbPointer which blocks all events, IgnorePointer is transparent to events. It is useful for overlay widgets that shouldn't intercept touches."
        },
        {
            "instruction": "What is the Table widget in Flutter?",
            "input": "",
            "output": "Table is a layout widget that displays children in rows and columns with customizable column widths. Unlike DataTable, it is a basic layout widget without headers, sorting, or selection. Column widths are defined using ColumnWidth subclasses: FlexColumnWidth, FixedColumnWidth, IntrinsicColumnWidth, and FractionColumnWidth. Each row is a TableRow containing TableCell widgets."
        },
        {
            "instruction": "What is the DataTable widget in Flutter?",
            "input": "",
            "output": "DataTable is a Material Design widget that displays data in a structured table with columns and rows. It supports sortable columns, selectable rows, and checkboxes. Columns are defined with DataColumn (label, sortable, tooltip) and rows with DataRow (cells, selected, onSelectChanged). It is suitable for displaying structured datasets but not optimized for large data — use PaginatedDataTable for that."
        },
        {
            "instruction": "What is the Autocomplete widget in Flutter?",
            "input": "",
            "output": "Autocomplete is a widget that provides text input suggestions based on user typing. It takes an optionsBuilder that returns matching options and an onSelected callback. The options appear in a dropdown overlay as the user types. It is customizable with optionsViewBuilder for custom option views and fieldViewBuilder for custom text fields."
        },
        {
            "instruction": "What is the SearchDelegate class in Flutter?",
            "input": "",
            "output": "SearchDelegate is an abstract class used with showSearch() to implement a full-screen search experience. It requires implementing buildActions(), buildLeading(), buildResults(), and buildSuggestions() methods. The search interface includes a search bar, back button, and configurable actions. It manages the search query state and provides a Material-styled search experience."
        },
        {
            "instruction": "What is the InteractiveViewer widget in Flutter?",
            "input": "",
            "output": "InteractiveViewer enables pan and zoom gestures on its child widget. It supports pinch-to-zoom, drag-to-pan, and optional boundary constraints. Properties include minScale, maxScale, boundaryMargin, and panEnabled. It is commonly used for zoomable images, maps, diagrams, and large content. The transformationController provides programmatic control over the transformation."
        },
        {
            "instruction": "What is the Overlay widget in Flutter?",
            "input": "",
            "output": "Overlay is a Stack-like widget that manages floating entries above other content. OverlayEntry objects are inserted into the Overlay and appear on top of the main widget tree. This is how tooltips, dropdown menus, and popup windows are implemented in Flutter. Overlay.of(context) accesses the nearest Overlay, and OverlayPortal provides a declarative API."
        },
        {
            "instruction": "What is the RepaintBoundary widget used for?",
            "input": "",
            "output": "RepaintBoundary creates an isolation layer in the rendering pipeline. When widgets inside a RepaintBoundary need repainting, only the subtree within the boundary is repainted, not the surrounding widgets. This is crucial for performance when parts of the UI update frequently (animations, timers) while the rest remains static."
        },
        {
            "instruction": "What is a SliverToBoxAdapter in Flutter?",
            "input": "",
            "output": "SliverToBoxAdapter wraps a regular box widget so it can be used inside a CustomScrollView. Since CustomScrollView only accepts sliver children, any non-sliver widget (like Container, Card, or Text) must be wrapped in SliverToBoxAdapter. It converts box layout constraints to sliver constraints, allowing any widget to participate in a sliver scroll layout."
        },
        {
            "instruction": "What is SliverPadding in Flutter?",
            "input": "",
            "output": "SliverPadding adds padding around a sliver child inside a CustomScrollView. It works like the Padding widget but for slivers. It takes an EdgeInsets padding and a sliver child. It is used to add spacing around SliverList, SliverGrid, or other slivers within the scroll view layout."
        },
        {
            "instruction": "What is the SliverGrid widget in Flutter?",
            "input": "",
            "output": "SliverGrid is a sliver that displays a grid of children inside a CustomScrollView. It takes a delegate for building children (SliverChildBuilderDelegate or SliverChildListDelegate) and a gridDelegate for layout (SliverGridDelegateWithFixedCrossAxisCount or SliverGridDelegateWithMaxCrossAxisExtent). It lazily builds items as they scroll into view."
        },
        {
            "instruction": "What is SliverList in Flutter?",
            "input": "",
            "output": "SliverList is a sliver that displays a linear list of children inside a CustomScrollView. It takes a delegate (SliverChildBuilderDelegate for lazy building or SliverChildListDelegate for a fixed list). It is the sliver equivalent of ListView and is used when you need to combine lists with other slivers like SliverAppBar or SliverGrid in one scroll view."
        },
        {
            "instruction": "What is the SliverFillRemaining widget?",
            "input": "",
            "output": "SliverFillRemaining fills the remaining visible space in a CustomScrollView with its child. It is useful for placing footer content or empty state messages at the bottom of a scroll view. The hasScrollBody property controls whether the child should be scrollable (true) or fill the remaining viewport (false)."
        },
        {
            "instruction": "What is the SliverPersistentHeader widget?",
            "input": "",
            "output": "SliverPersistentHeader creates a header that can remain pinned or floating at the top of a CustomScrollView. It takes a SliverPersistentHeaderDelegate that defines minExtent, maxExtent, and the build method. It is used for creating sticky section headers, collapsible headers, and custom scrolling effects beyond what SliverAppBar provides."
        },
        {
            "instruction": "What is the NestedScrollView widget in Flutter?",
            "input": "",
            "output": "NestedScrollView coordinates scrolling between a header (SliverAppBar) and a body containing its own scroll view (like a TabBarView with ListViews). It connects the outer and inner scroll controllers to provide a unified scroll experience. Without NestedScrollView, nested scrollable widgets would conflict and produce poor scroll behavior."
        },
        {
            "instruction": "What is WidgetSpan in Flutter?",
            "input": "",
            "output": "WidgetSpan is a type of InlineSpan that embeds a widget inline within a RichText paragraph. Unlike TextSpan which only handles text, WidgetSpan can include icons, images, buttons, or any widget alongside text. The child widget is aligned with the text using PlaceholderAlignment options like baseline, middle, or aboveBaseline."
        },
        {
            "instruction": "What is the InkResponse widget in Flutter?",
            "input": "",
            "output": "InkResponse is the base class for ink splash effects in Material Design. InkWell extends it with a rectangular splash area. InkResponse allows customizing the splash shape, radius, highlight shape, and containment. It responds to taps, long presses, and provides visual feedback through ink ripple animations. It requires a Material widget ancestor."
        },
        {
            "instruction": "What are implicit animations in Flutter? Give examples.",
            "input": "",
            "output": "Implicit animations are widgets that automatically animate changes to their properties over a specified duration. Examples include: AnimatedContainer (size, color, padding), AnimatedOpacity (transparency), AnimatedPadding (padding), AnimatedPositioned (position in Stack), AnimatedAlign (alignment), AnimatedCrossFade (cross-fading between two children), AnimatedDefaultTextStyle (text style), and AnimatedSwitcher (switching between widgets)."
        },
        {
            "instruction": "What is the AnimatedSwitcher widget in Flutter?",
            "input": "",
            "output": "AnimatedSwitcher transitions between two widgets by animating the old widget out and the new widget in. It uses a fade transition by default but supports custom transitions via transitionBuilder. The child is identified by key — when the key changes, AnimatedSwitcher animates the switch. It is useful for switching icons, text, or entire views with animation."
        },
        {
            "instruction": "What is the AnimatedCrossFade widget in Flutter?",
            "input": "",
            "output": "AnimatedCrossFade cross-fades between two child widgets based on a CrossFadeState value (showFirst or showSecond). It smoothly transitions opacity and size between the two children over a specified duration. It is commonly used for toggling between a loading indicator and content, or switching between two views with a smooth animated transition."
        },
        {
            "instruction": "What is the Hero widget in Flutter?",
            "input": "",
            "output": "Hero creates a shared element transition animation between two screens. When navigating from one screen to another, a widget with the same Hero tag flies from its old position to its new position. The tag must be unique within each screen. It is commonly used for image thumbnails that expand when tapped, or profile avatars transitioning between list and detail views."
        },
        {
            "instruction": "What is the Tooltip widget in Flutter?",
            "input": "",
            "output": "Tooltip displays a brief, informative message when the user long-presses or hovers over a widget. It wraps a child widget and shows the message in a floating label. The message, height, padding, margin, vertical offset, and decoration are customizable. Tooltips improve accessibility by providing descriptions for icon-only buttons."
        },
        {
            "instruction": "What is the Chip widget in Flutter?",
            "input": "",
            "output": "Chip is a compact Material Design element representing an attribute, action, or filter. Variants include InputChip (user input), ChoiceChip (single selection), FilterChip (multi selection), and ActionChip (trigger action). Each supports label, avatar, delete icon, and styling. Chips are commonly used in tag selection, filter bars, and contact entries."
        },
        {
            "instruction": "What is the Badge widget in Flutter?",
            "input": "",
            "output": "Badge is a Material 3 widget that displays a small notification indicator (dot or count) on another widget. It is typically used on icons in navigation bars to indicate unread notifications. It supports customizable label, background color, text color, offset, and padding. Badge wraps its child with the indicator positioned at the top-right corner."
        },
        {
            "instruction": "What is the SegmentedButton widget in Flutter?",
            "input": "",
            "output": "SegmentedButton is a Material 3 widget that displays a set of toggleable segments. Users can select one or multiple segments. Each segment is defined with a ButtonSegment containing a value, label, and optional icon. The selected property holds the current selection set. It replaces the older ToggleButtons widget with Material 3 design."
        },
        {
            "instruction": "What is the NavigationBar widget in Flutter?",
            "input": "",
            "output": "NavigationBar is the Material 3 replacement for BottomNavigationBar. It displays 3-5 NavigationDestination items at the bottom of the screen for top-level navigation. It supports a selectedIndex, onDestinationSelected callback, and customizable appearance. Each destination has an icon, selectedIcon, and label. It automatically adds a pill-shaped indicator around the selected item."
        },
        {
            "instruction": "What is the NavigationRail widget in Flutter?",
            "input": "",
            "output": "NavigationRail is a vertical navigation component displayed along the left or right side of the screen. It is ideal for tablet and desktop layouts where a side navigation is preferable to a bottom bar. It contains NavigationRailDestination items with icons and labels. It supports extended mode, leading/trailing widgets, and group alignment."
        },
        {
            "instruction": "What is the NavigationDrawer widget in Flutter?",
            "input": "",
            "output": "NavigationDrawer is a Material 3 navigation component that slides in from the side. Unlike the basic Drawer, it provides NavigationDrawerDestination items with icons and labels, and supports a selectedIndex and onDestinationSelected callback. It is designed for apps with 5+ top-level destinations and can be permanent on larger screens."
        },
        {
            "instruction": "What is the BottomSheet widget in Flutter?",
            "input": "",
            "output": "BottomSheet is a panel that slides up from the bottom of the screen. Flutter provides two types: showModalBottomSheet (blocks background interaction) and showBottomSheet (persistent, allows interaction). Bottom sheets are used for additional content, actions, or filters. They can be dragged to dismiss and support custom shapes, drag handles, and scroll behavior."
        },
        {
            "instruction": "What is the ExpansionTile widget in Flutter?",
            "input": "",
            "output": "ExpansionTile is a ListTile that expands to reveal additional content when tapped. It has a title, leading, trailing (defaults to expand/collapse arrow), and children that are shown or hidden. It supports initiallyExpanded, onExpansionChanged callback, and expansion animation. It is commonly used in settings pages, FAQ sections, and collapsible list groups."
        },
        {
            "instruction": "What is the Stepper widget in Flutter?",
            "input": "",
            "output": "Stepper displays a sequence of steps that guide the user through a multi-step process. Each Step has title, content, subtitle, and state (indexed, editing, complete, disabled, error). Stepper supports vertical and horizontal layouts, onStepContinue, onStepCancel, and onStepTapped callbacks. It manages the current step index and provides navigation buttons."
        },
        {
            "instruction": "What is the TabBar widget in Flutter?",
            "input": "",
            "output": "TabBar displays a horizontal row of tabs typically placed below an AppBar. It works with TabBarView to display corresponding content for each tab. It requires a TabController (or DefaultTabController ancestor). Each tab is defined with Tab widget containing text, icon, or both. TabBar supports scrolling, custom indicators, and label styling."
        },
        {
            "instruction": "What is the TabBarView widget in Flutter?",
            "input": "",
            "output": "TabBarView displays the content corresponding to the selected tab in a TabBar. It takes a list of children (one per tab) and swipes horizontally between them. It requires the same TabController as its associated TabBar. The controller synchronizes tab selection with the displayed view, enabling swipe gestures and programmatic navigation."
        },
        {
            "instruction": "What is the DefaultTabController widget in Flutter?",
            "input": "",
            "output": "DefaultTabController is a convenience widget that creates and manages a TabController for its descendants. It takes a length (number of tabs) and provides the controller to TabBar and TabBarView widgets in the subtree. It eliminates the need to create a TabController manually and manage SingleTickerProviderStateMixin in the state class."
        },
        {
            "instruction": "What is the PageView widget in Flutter?",
            "input": "",
            "output": "PageView is a scrollable list that works page by page, snapping to full pages. It supports horizontal and vertical scrolling. Each page fills the viewport. PageController controls the initial page, viewport fraction, and provides methods like jumpToPage(), animateToPage(), and nextPage(). It is used for onboarding flows, image galleries, and swipable card interfaces."
        },
        {
            "instruction": "What is the FittedBox widget in Flutter?",
            "input": "",
            "output": "FittedBox scales and positions its child within itself according to a BoxFit value. Common fits: contain (scale to fit fully), cover (fill, may crop), fitWidth, fitHeight, fill (stretch), and none. It is useful for making text or images fit within constrained spaces without overflow, especially when the content size is unknown."
        },
        {
            "instruction": "What is the FractionallySizedBox widget in Flutter?",
            "input": "",
            "output": "FractionallySizedBox sizes its child to a fraction of the available space. widthFactor: 0.5 makes the child half the parent's width. heightFactor: 0.8 makes it 80% of the parent's height. It is useful for responsive layouts where a widget should be a percentage of the available space. When used in Row/Column, wrap it in Flexible."
        },
        {
            "instruction": "What is the LimitedBox widget in Flutter?",
            "input": "",
            "output": "LimitedBox imposes maximum width and height constraints on its child only when the incoming constraints are unbounded. It is used inside scrollable widgets where children would otherwise have infinite extent. For example, in a ListView, a Container without height has unbounded constraints — LimitedBox limits it to maxHeight while still allowing normal sizing in bounded contexts."
        },
        {
            "instruction": "What is the ConstrainedBox widget in Flutter?",
            "input": "",
            "output": "ConstrainedBox imposes additional BoxConstraints on its child. It can set minimum and maximum width and height. Unlike SizedBox which sets exact dimensions, ConstrainedBox defines a range. The child's final size is the intersection of the parent's constraints and the ConstrainedBox constraints. It is useful for setting minimum tap targets or maximum content widths."
        },
        {
            "instruction": "What is the UnconstrainedBox widget in Flutter?",
            "input": "",
            "output": "UnconstrainedBox removes all constraints from its child, allowing the child to determine its own size. If the child overflows the parent's bounds, overflow indicators appear in debug mode. It is useful when a child widget needs to escape parent constraints, such as displaying an image at its natural size regardless of the container."
        },
        {
            "instruction": "What is the OverflowBox widget in Flutter?",
            "input": "",
            "output": "OverflowBox is a widget that imposes different constraints on its child than it receives from its parent, potentially allowing the child to overflow. Unlike UnconstrainedBox, it does not show overflow warnings. It is useful for creating visual effects where content intentionally extends beyond its allocated space, such as overlapping decorations."
        },
        {
            "instruction": "What is the Transform widget in Flutter?",
            "input": "",
            "output": "Transform applies a matrix transformation to its child during painting. It supports rotation (Transform.rotate), scaling (Transform.scale), translation (Transform.translate), and arbitrary 4D matrix transformations. Transforms are applied during painting, not during layout — the child still occupies its original layout space. Use the alignment property to set the transformation origin."
        },
        {
            "instruction": "What is the RotatedBox widget in Flutter?",
            "input": "",
            "output": "RotatedBox rotates its child by a number of quarter turns (0-3) during layout, not just painting. Unlike Transform.rotate which only rotates visually while keeping the original layout bounds, RotatedBox actually changes the layout size to match the rotated dimensions. This means surrounding widgets properly account for the rotated size."
        },
        {
            "instruction": "What is the Baseline widget in Flutter?",
            "input": "",
            "output": "Baseline positions its child such that the child's baseline is at a specified distance from the top. It is used to align text or widgets to a common baseline, ensuring proper vertical alignment. The baseline property specifies the distance, and baselineType specifies whether to use alphabetic or ideographic baseline."
        },
        {
            "instruction": "What is a Flutter plugin vs a Flutter package?",
            "input": "",
            "output": "A Flutter package is a Dart-only library that contains reusable code, widgets, or utilities. A Flutter plugin is a specialized package that includes platform-specific code (Kotlin/Java, Swift/Objective-C, C++) to access native device features like camera, GPS, or Bluetooth. All plugins are packages, but not all packages are plugins."
        },
        {
            "instruction": "What does flutter upgrade do?",
            "input": "",
            "output": "flutter upgrade updates both the Flutter SDK and the Dart SDK to the latest stable version. It fetches the latest code from the Flutter repository, rebuilds the Flutter tools, and may download new engine artifacts. After upgrading, run flutter pub get in your projects to update dependencies. Use flutter downgrade to revert if needed."
        },
        {
            "instruction": "What is the flutter run command?",
            "input": "",
            "output": "flutter run compiles and launches the Flutter app on a connected device or emulator. It defaults to debug mode with hot reload support. Common flags: -d (specify device), --release (release mode), --profile (profile mode), --verbose (detailed logs). During debug mode, press 'r' for hot reload, 'R' for hot restart, and 'q' to quit."
        },
        {
            "instruction": "What is the Divider widget in Flutter?",
            "input": "",
            "output": "Divider is a thin horizontal line used to separate content in lists and layouts. It has height (total space including the line), thickness (line thickness), color, indent, and endIndent properties. VerticalDivider provides a vertical equivalent. They follow the Material Design guidelines for visual separation of content sections."
        },
        {
            "instruction": "What is the Spacer widget in Flutter?",
            "input": "",
            "output": "Spacer is a flexible widget that occupies available space in a Row, Column, or Flex layout. It is equivalent to an empty Expanded widget. The flex property controls how much space to take relative to other Spacers. It is commonly used to push widgets apart: Row(children: [Text('Left'), Spacer(), Text('Right')]) places text at opposite ends."
        },
        {
            "instruction": "What is the RefreshIndicator widget in Flutter?",
            "input": "",
            "output": "RefreshIndicator wraps a scrollable widget and shows a Material Design pull-to-refresh spinner when the user overscrolls. It requires an onRefresh callback that returns a Future — the spinner persists until the Future completes. It is commonly used with ListView to reload data from an API. The child must be scrollable for the gesture to work."
        },
        {
            "instruction": "What is the Flow widget in Flutter?",
            "input": "",
            "output": "Flow is a layout widget that positions children using a FlowDelegate. The delegate's paintChildren method positions each child using transformation matrices. Flow is highly efficient because it can reposition children without triggering layout — only a repaint. It is used for complex animated layouts like expandable menus and custom flow layouts."
        },
        {
            "instruction": "What is the focus system in Flutter?",
            "input": "",
            "output": "Flutter's focus system manages which widget receives keyboard events. FocusNode represents a focusable widget, FocusScope groups focus nodes, and FocusScopeNode manages focus within a scope. Focus widget wraps focusable children. FocusManager controls the global focus state. The system supports traversal, automatic focus, and skip-focus for accessibility navigation."
        },
        {
            "instruction": "What is the LayoutBuilder widget in Flutter?",
            "input": "",
            "output": "LayoutBuilder is a builder widget that provides the parent's BoxConstraints to its builder function. This allows the child to adapt its layout based on available space. It is the foundation of responsive design in Flutter — you can change the number of columns, switch between layouts, or hide widgets based on maxWidth and maxHeight constraints."
        },
        {
            "instruction": "What is the OrientationBuilder widget in Flutter?",
            "input": "",
            "output": "OrientationBuilder provides the current device orientation (portrait or landscape) to its builder function. It rebuilds when the orientation changes. It is simpler than MediaQuery for orientation-only logic. The orientation is determined by comparing width and height constraints — if width > height, it is landscape, otherwise portrait."
        },
        {
            "instruction": "What is the GestureDetector widget in Flutter?",
            "input": "",
            "output": "GestureDetector detects gestures made on its child widget, including taps (onTap, onDoubleTap, onLongPress), drags (onPanUpdate, onHorizontalDragUpdate, onVerticalDragUpdate), and scale (onScaleUpdate). It does not provide visual feedback — use InkWell for Material tap effects. GestureDetector supports hit testing behavior and gesture disambiguation."
        },
        {
            "instruction": "What is the ListTile widget in Flutter?",
            "input": "",
            "output": "ListTile is a fixed-height Material Design row widget commonly used in ListView. It has slots for leading (icon/avatar), title, subtitle, trailing (icon/button), and supports onTap and onLongPress. It follows Material specifications for spacing and sizing. Variants include CheckboxListTile, SwitchListTile, RadioListTile, and ExpansionTile."
        },
        {
            "instruction": "What is the Card widget in Flutter?",
            "input": "",
            "output": "Card is a Material Design surface with elevation, rounded corners, and optional shadow. It wraps content to create a distinct visual grouping. Key properties include elevation, shape (default RoundedRectangleBorder), color, margin, and clipBehavior. In Material 3, Card comes in three variants: Card (filled), Card.outlined, and Card (elevated with shadow)."
        },
        {
            "instruction": "What is the SnackBar widget in Flutter?",
            "input": "",
            "output": "SnackBar is a lightweight message that appears briefly at the bottom of the screen. It is shown using ScaffoldMessenger.of(context).showSnackBar(). It supports content (usually Text), action button, duration, behavior (fixed or floating), shape, and dismiss direction. SnackBars should be brief and non-critical since they auto-dismiss. SnackBarAction adds an interactive button."
        },
        {
            "instruction": "What is the AlertDialog widget in Flutter?",
            "input": "",
            "output": "AlertDialog is a Material Design dialog that appears centered on the screen with a dimmed background. It has title, content, and actions (buttons) slots. It is shown using showDialog() which returns a Future that resolves when the dialog is dismissed. The barrierDismissible parameter controls whether tapping outside closes the dialog."
        },
        {
            "instruction": "What is the SimpleDialog widget in Flutter?",
            "input": "",
            "output": "SimpleDialog is a Material Design dialog that presents a list of options. Each option is a SimpleDialogOption widget with an onPressed callback. Unlike AlertDialog which has action buttons, SimpleDialog is designed for selection from multiple choices. It is shown with showDialog() and typically pops with Navigator.pop(context, selectedValue)."
        },
        {
            "instruction": "What is the showDialog function in Flutter?",
            "input": "",
            "output": "showDialog() displays a Material Design dialog above the current content. It takes a BuildContext and a builder that returns the dialog widget. It returns a Future<T?> that completes when the dialog is closed. Key parameters include barrierDismissible, barrierColor, and useRootNavigator. The dialog is closed via Navigator.pop(context) or tapping the barrier."
        },
        {
            "instruction": "What is the PopupMenuButton widget in Flutter?",
            "input": "",
            "output": "PopupMenuButton displays a three-dot menu that shows a popup menu with selectable items. It takes itemBuilder that returns a list of PopupMenuItem widgets and an onSelected callback. Each item has a value and child widget. It is commonly used in AppBar actions for overflow menus. The menu position adjusts based on available screen space."
        },
        {
            "instruction": "What is the Semantics widget in Flutter?",
            "input": "",
            "output": "Semantics provides accessibility information about a widget to screen readers and assistive technologies. It annotates widgets with labels, hints, values, and actions that describe their purpose and state. Semantics is crucial for making apps accessible to users with disabilities. Many built-in widgets include semantics automatically, but custom widgets may need explicit annotation."
        },
        {
            "instruction": "What is the ExcludeSemantics widget in Flutter?",
            "input": "",
            "output": "ExcludeSemantics removes its child from the semantics tree, making it invisible to screen readers and assistive technologies. It is used when decorative elements (dividers, images) don't need accessibility labels. Use MergeSemantics to combine multiple semantic nodes into one. Both help create a clean, navigable accessibility experience."
        },
        {
            "instruction": "What is the Visibility widget in Flutter?",
            "input": "",
            "output": "Visibility controls whether its child is visible, rendered, and interactive. When visible is false, it removes the child from painting and hit testing. The maintainSize, maintainAnimation, maintainState, and maintainInteractivity properties control what is preserved when hidden. Unlike Opacity(opacity: 0) which still occupies space, Visibility can completely remove the widget."
        },
        {
            "instruction": "What is the Offstage widget in Flutter?",
            "input": "",
            "output": "Offstage hides a widget from the visual tree while keeping it in the widget tree. When offstage is true, the widget is not painted, not hit-testable, and does not take up space, but it still participates in layout and state is maintained. It is useful when you need to hide a widget temporarily while preserving its state."
        },
        {
            "instruction": "What is the IntrinsicHeight widget in Flutter?",
            "input": "",
            "output": "IntrinsicHeight sizes its child to the child's intrinsic height. It is commonly used in Row to make all children the same height as the tallest child, which Row doesn't do by default. It should be used sparingly as it is O(N^2) in layout cost. Prefer Expanded, Flexible, or CrossAxisAlignment.stretch for simpler cases."
        },
        {
            "instruction": "What is the IntrinsicWidth widget in Flutter?",
            "input": "",
            "output": "IntrinsicWidth sizes its child to the child's intrinsic width. It is commonly used to make a Column's children all the same width as the widest child. Like IntrinsicHeight, it has O(N^2) layout cost and should be used sparingly. It is useful for dialogs and menus where content needs to size to the widest item."
        },
        {
            "instruction": "What is the ColorFiltered widget in Flutter?",
            "input": "",
            "output": "ColorFiltered applies a ColorFilter to its child widget. Common filters include grayscale (ColorFilter.matrix with grayscale matrix), color overlay (ColorFilter.mode with blend mode), and custom color matrices. It is useful for creating disabled states, theming effects, or artistic color manipulations on images and widgets."
        },
        {
            "instruction": "What is the ImageFiltered widget in Flutter?",
            "input": "",
            "output": "ImageFiltered applies an ImageFilter to its child widget. The most common usage is ImageFilter.blur() for blurring the child. Unlike BackdropFilter which blurs content behind the widget, ImageFiltered blurs the widget itself. It is useful for creating blurred overlays, frosted effects on specific widgets, and visual blur animations."
        },
        {
            "instruction": "What is the Flutter DevTools?",
            "input": "",
            "output": "Flutter DevTools is a suite of debugging and performance tools for Flutter apps. It provides: Widget Inspector for exploring the widget tree, Performance view for analyzing frame rendering, CPU Profiler for identifying slow functions, Memory view for tracking allocations, Network view for HTTP requests, and Logging view for debug messages. It runs in a browser alongside the debug session."
        },
        {
            "instruction": "What is the MediaQuery class in Flutter?",
            "input": "",
            "output": "MediaQuery provides information about the current device and display. MediaQuery.of(context) returns MediaQueryData containing size (screen dimensions), padding (system UI insets), viewInsets (keyboard), textScaleFactor, platformBrightness, and more. It is essential for responsive design. Use MediaQuery.sizeOf(context) for better rebuild performance when only size is needed."
        },
        {
            "instruction": "What is an asset in Flutter?",
            "input": "",
            "output": "Assets are files bundled with the app at build time, including images, fonts, JSON files, and other data. They are declared in pubspec.yaml under the flutter: assets: section. Images support resolution variants (2.0x, 3.0x folders). Assets are loaded at runtime using rootBundle.loadString() for text, Image.asset() for images, and similar APIs for other types."
        },
        {
            "instruction": "How do you add custom fonts in Flutter?",
            "input": "",
            "output": "Custom fonts are added by placing font files (.ttf, .otf) in a project folder (e.g., assets/fonts/), then declaring them in pubspec.yaml under flutter: fonts: with family name and asset paths including weight and style variants. Use the font with TextStyle(fontFamily: 'FontName'). Google Fonts can be used via the google_fonts package without manual setup."
        },
        {
            "instruction": "What is the ClipRRect widget in Flutter?",
            "input": "",
            "output": "ClipRRect clips its child using a rounded rectangle. It takes a borderRadius parameter that defines the corner radius. It is commonly used to create rounded corners on images, containers, and other widgets. ClipOval creates a circular clip, ClipRect clips to a rectangle, and ClipPath clips to a custom path shape."
        },
        {
            "instruction": "What is the ClipOval widget in Flutter?",
            "input": "",
            "output": "ClipOval clips its child to an oval (or circle if the child is square). It is commonly used to create circular images and avatars. For example, wrapping an Image widget in ClipOval creates a circular profile picture. For rounded rectangles, use ClipRRect instead. For custom shapes, use ClipPath with a custom path."
        },
        {
            "instruction": "What is the Opacity widget in Flutter?",
            "input": "",
            "output": "Opacity makes its child partially transparent by applying an opacity value between 0.0 (invisible) and 1.0 (fully visible). Unlike Visibility, Opacity keeps the widget in the layout — it still occupies space. Use AnimatedOpacity for smooth opacity transitions. Note: Opacity can be expensive for complex children — prefer using color opacity when possible."
        },
        {
            "instruction": "What is the flutter_lints package?",
            "input": "",
            "output": "flutter_lints (now flutter_lints is replaced by the official 'flutter_lints' or 'lints' package) provides recommended lint rules for Flutter and Dart projects. Lint rules are defined in analysis_options.yaml and enforce code style, best practices, and error prevention. The recommended set includes rules for avoiding common mistakes, unused code, and style consistency."
        },
        {
            "instruction": "What is the flutter format command?",
            "input": "",
            "output": "dart format (formerly flutter format) automatically formats Dart code to follow standard formatting conventions. It ensures consistent indentation, spacing, and line breaks. It is typically run as 'dart format .' to format all files in the project. Many IDEs run it automatically on save. It follows the dart_style package conventions."
        },
        {
            "instruction": "What is a mixin in Dart?",
            "input": "",
            "output": "A mixin is a way to reuse code across multiple class hierarchies without inheritance. Mixins are declared with the mixin keyword and applied using the with keyword: class MyClass with MixinA, MixinB. Mixins can have methods and fields but cannot be instantiated. The on keyword restricts a mixin to specific superclasses. Mixins solve the diamond problem of multiple inheritance."
        },
        {
            "instruction": "What is the difference between const and final in Dart?",
            "input": "",
            "output": "Both const and final create variables that can only be assigned once, but const requires compile-time constant values while final allows runtime assignment. const creates deeply immutable objects — all nested fields must also be const. final objects can have mutable fields. const objects are canonicalized (shared across the app). Use const for literals and final for runtime values."
        },
        {
            "instruction": "What are Dart enums and how are enhanced enums different?",
            "input": "",
            "output": "Enums define a fixed set of named constants. Basic enums: enum Color { red, green, blue }. Enhanced enums (Dart 2.17+) can have fields, methods, constructors, and implement interfaces: enum Color { red(0xFF0000); const Color(this.value); final int value; }. Enhanced enums enable richer behavior on enumerated types while maintaining exhaustive switch checks."
        },
        {
            "instruction": "What is the late keyword in Dart?",
            "input": "",
            "output": "The late keyword in Dart declares a non-nullable variable that is initialized after its declaration. late final name = computeName() enables lazy initialization — computed only on first access. late also allows non-nullable instance variables to be set in initState() rather than the constructor. The runtime throws LateInitializationError if a late variable is accessed before assignment."
        },
        {
            "instruction": "What is the typedef keyword in Dart?",
            "input": "",
            "output": "typedef creates a type alias for function signatures or other types. For functions: typedef IntCallback = void Function(int value). For types: typedef StringList = List<String>. Type aliases improve code readability and allow complex types to be reused. In Dart 2.13+, typedef can alias any type, not just function types."
        },
        {
            "instruction": "What is a factory constructor in Dart?",
            "input": "",
            "output": "A factory constructor uses the factory keyword and doesn't always create a new instance. It can return cached instances, subtype instances, or computed instances. Unlike regular constructors, factory constructors can have return statements. They are used for the singleton pattern, instance caching, and returning subclass instances based on input parameters."
        },
        # ─── More Basic Questions (Batch 4) ─────────────────────────────
        {
            "instruction": "What is the difference between Container and SizedBox?",
            "input": "",
            "output": "SizedBox is a simpler widget that only sets width and height constraints. Container is a convenience widget that combines padding, margin, decoration, alignment, constraints, and transform. Use SizedBox when you only need to set dimensions (it is more efficient). Use Container when you need decoration, padding, or other visual properties. SizedBox.expand makes the child fill all available space."
        },
        {
            "instruction": "What is the difference between Positioned and Align in a Stack?",
            "input": "",
            "output": "Positioned uses absolute pixel offsets (top, left, right, bottom) to position a child in a Stack. Align uses relative alignment values (Alignment.center, Alignment(0.5, -1.0)) that are proportional to the Stack's size. Use Positioned for exact pixel placement and Align for proportional or alignment-based placement. Positioned can also set width and height."
        },
        {
            "instruction": "What is the AspectRatio widget in Flutter?",
            "input": "",
            "output": "AspectRatio forces its child to maintain a specific width-to-height ratio. It takes an aspectRatio property (width/height, e.g., 16/9 for widescreen). The widget first tries to maximize the width, then adjusts height to maintain the ratio within the constraints. It is commonly used for videos, images, and responsive card layouts."
        },
        {
            "instruction": "What is the Center widget in Flutter?",
            "input": "",
            "output": "Center is a convenience widget that aligns its child to the center of the available space. It is equivalent to Align(alignment: Alignment.center). It expands to fill the parent by default. The widthFactor and heightFactor properties can shrink-wrap the Center around its child. Center is one of the most commonly used layout widgets in Flutter."
        },
        {
            "instruction": "What is the Align widget in Flutter?",
            "input": "",
            "output": "Align positions its child within itself using an Alignment value. Alignment(-1, -1) is top-left, (1, 1) is bottom-right, (0, 0) is center. It also supports named constants like Alignment.topCenter, Alignment.bottomRight. widthFactor and heightFactor control the Align widget's own size relative to the child. It expands to fill the parent by default."
        },
        {
            "instruction": "What is the Padding widget in Flutter?",
            "input": "",
            "output": "Padding adds empty space around its child widget. It takes an EdgeInsets value specifying padding on each side: EdgeInsets.all(16) for uniform padding, EdgeInsets.symmetric(horizontal: 8, vertical: 4) for symmetric padding, EdgeInsets.only(left: 16, top: 8) for specific sides. Padding is implemented as a single-child rendering widget."
        },
        {
            "instruction": "What is the Row widget in Flutter?",
            "input": "",
            "output": "Row arranges its children horizontally in a single line. It uses mainAxisAlignment for horizontal distribution and crossAxisAlignment for vertical alignment. Children can be Expanded or Flexible for proportional sizing. mainAxisSize.min shrinks the Row to fit its children. Row does not scroll — use SingleChildScrollView with a Row for horizontal scrolling."
        },
        {
            "instruction": "What is the Column widget in Flutter?",
            "input": "",
            "output": "Column arranges its children vertically in a single line. It uses mainAxisAlignment for vertical distribution and crossAxisAlignment for horizontal alignment. Like Row, children can use Expanded or Flexible. Columns do not scroll — wrap in SingleChildScrollView for scrolling. Column takes up full height by default; use mainAxisSize.min to shrink."
        },
        {
            "instruction": "What is the Stack widget in Flutter?",
            "input": "",
            "output": "Stack overlays its children on top of each other, with the last child on top. Children can be positioned using Positioned widget for absolute placement or Align for alignment-based placement. Non-positioned children fill the Stack by default. The fit property controls how non-positioned children are sized: loose (own size) or expand (fill Stack). Stack is used for overlapping layouts."
        },
        {
            "instruction": "What is the GridView widget in Flutter?",
            "input": "",
            "output": "GridView displays items in a 2D scrollable grid. GridView.count uses a fixed cross-axis count. GridView.extent specifies maximum item width. GridView.builder lazily builds items (efficient for large grids). GridView.custom uses custom delegate. The gridDelegate controls item sizing: SliverGridDelegateWithFixedCrossAxisCount or SliverGridDelegateWithMaxCrossAxisExtent."
        },
        {
            "instruction": "What is the ListView widget in Flutter?",
            "input": "",
            "output": "ListView is the most commonly used scrollable widget. ListView() takes a list of children (builds all at once). ListView.builder lazily builds items with an itemBuilder and itemCount (efficient for large lists). ListView.separated adds separators between items. ListView.custom uses a custom SliverChildDelegate. ListView scrolls vertically by default; set scrollDirection for horizontal."
        },
        {
            "instruction": "What is the difference between ListView and ListView.builder?",
            "input": "",
            "output": "ListView() takes a direct list of children and builds all of them immediately, even off-screen ones. ListView.builder uses an itemBuilder callback to lazily create items only when they are about to appear on screen. Use ListView for short, fixed lists. Use ListView.builder for long or dynamic lists to save memory and improve performance."
        },
        {
            "instruction": "What is the TextField widget in Flutter?",
            "input": "",
            "output": "TextField is the primary text input widget. It uses a TextEditingController for text management, InputDecoration for visual styling, onChanged for value updates, and TextInputType for keyboard type. It supports obscureText for passwords, maxLines for multiline, inputFormatters for input filtering, and autofillHints for autofill. TextFormField adds Form integration with validation."
        },
        {
            "instruction": "What is the TextFormField widget in Flutter?",
            "input": "",
            "output": "TextFormField is a TextField that integrates with the Form widget. It adds a validator function for validation, onSaved callback for form submission, and autovalidateMode for automatic validation timing. When Form.validate() is called, all TextFormField validators run. It provides the same functionality as TextField plus form-specific features."
        },
        {
            "instruction": "What is the ElevatedButton widget in Flutter?",
            "input": "",
            "output": "ElevatedButton is a Material Design filled button with elevation. It has a visual lift effect and is the primary action button style. It takes onPressed callback and child widget. Style with ElevatedButton.styleFrom() for color, elevation, shape, padding. When onPressed is null, the button is disabled with reduced opacity. It replaced the deprecated RaisedButton."
        },
        {
            "instruction": "What is the TextButton widget in Flutter?",
            "input": "",
            "output": "TextButton is a Material Design flat button without elevation. It is used for less prominent actions, typically in dialogs, cards, and inline with other content. It has minimal visual weight. Style with TextButton.styleFrom() for color, text style, and shape. When onPressed is null, the button is disabled. It replaced the deprecated FlatButton."
        },
        {
            "instruction": "What is the OutlinedButton widget in Flutter?",
            "input": "",
            "output": "OutlinedButton is a Material Design button with a visible border but no fill color. It is used for medium-emphasis actions, more prominent than TextButton but less than ElevatedButton. It displays an outline border by default. Style with OutlinedButton.styleFrom() for border style, color, and shape. It replaced the deprecated OutlineButton."
        },
        {
            "instruction": "What is the IconButton widget in Flutter?",
            "input": "",
            "output": "IconButton is a tappable icon that responds with an ink splash effect. It takes an icon and onPressed callback. It has a default padding and minimum tap area of 48x48 pixels for accessibility. The splashRadius controls the ink effect size. tooltip provides accessibility description. color and disabledColor control appearance. It is commonly used in AppBar actions."
        },
        {
            "instruction": "What is the FloatingActionButton widget in Flutter?",
            "input": "",
            "output": "FloatingActionButton (FAB) is a circular Material button that floats above content, typically used for the primary action on a screen. It is placed in Scaffold's floatingActionButton property. Variants: regular (56x56), small (40x40), large (96x96), and extended (adds a label). Position with floatingActionButtonLocation. It provides elevation and ink splash effects."
        },
        {
            "instruction": "What is the Scaffold's AppBar property?",
            "input": "",
            "output": "Scaffold's appBar property accepts a PreferredSizeWidget, typically an AppBar or SliverAppBar. AppBar provides a title, leading icon (back/menu), actions (icon buttons), bottom (TabBar), and flexible space. It uses the theme's primary color by default. AppBar.automaticallyImplyLeading adds a back button when there is a previous route. CupertinoNavigationBar provides iOS-style navigation."
        },
        {
            "instruction": "What is the showModalBottomSheet function in Flutter?",
            "input": "",
            "output": "showModalBottomSheet displays a modal bottom sheet that slides up from the bottom of the screen and dims the background. It returns a Future that resolves when dismissed. Key parameters: builder (content), isScrollControlled (full height), enableDrag, backgroundColor, shape, and showDragHandle. The sheet is dismissed by tapping the barrier, swiping down, or calling Navigator.pop."
        },
        {
            "instruction": "What is the CupertinoAlertDialog widget in Flutter?",
            "input": "",
            "output": "CupertinoAlertDialog displays an iOS-style alert dialog with title, content, and a list of CupertinoDialogAction buttons. It uses the iOS design language with blurred background and rounded corners. Show with showCupertinoDialog(). It is used when the app needs to match iOS native dialog appearance instead of Material Design dialogs."
        },
        {
            "instruction": "What is the CupertinoTextField widget in Flutter?",
            "input": "",
            "output": "CupertinoTextField displays an iOS-style text input field with rounded rectangle border and placeholder text. It provides padding, prefix, suffix, clearButtonMode for a clear button, and decoration for customization. It mimics UITextField from iOS. Use CupertinoSearchTextField for iOS-style search inputs. It is used in CupertinoApp or when matching iOS design language."
        },
        {
            "instruction": "What is the difference between MaterialApp and WidgetsApp?",
            "input": "",
            "output": "WidgetsApp is the base class that provides fundamental app features: navigation, localization, and media query. MaterialApp extends WidgetsApp and adds Material Design specific features: ThemeData, Material-styled dialogs, Scaffold support, and additional Material utilities. CupertinoApp extends WidgetsApp with iOS-specific features. Use WidgetsApp for custom design systems without Material or Cupertino."
        },
        {
            "instruction": "What is an enum in Dart?",
            "input": "",
            "output": "An enum (enumeration) in Dart defines a type with a fixed set of named constants: enum Status { active, inactive, pending }. Enum values are accessed as Status.active. Use enum with switch statements for exhaustive handling. Enums have index property and values list. In Dart 2.17+, enhanced enums support fields, methods, and constructors."
        },
        {
            "instruction": "What is the spread operator in Dart?",
            "input": "",
            "output": "The spread operator (...) inserts all elements of one collection into another: [1, 2, ...otherList, 5]. It works with Lists, Sets, and Maps. The null-aware spread (...?) handles null collections: [...?nullableList]. It is heavily used in Flutter to compose widget lists conditionally: Column(children: [...widgets1, if (show) ...widgets2])."
        },
        {
            "instruction": "What are getters and setters in Dart?",
            "input": "",
            "output": "Getters and setters control access to object properties. Getters use get keyword: String get fullName => '$first $last'. Setters use set keyword: set fullName(String value) { ... }. They look like field access but execute code. Dart creates implicit getters/setters for all fields. Custom getters enable computed properties. Setters enable validation on assignment."
        },
        {
            "instruction": "What is the cascade notation (..) in Dart?",
            "input": "",
            "output": "Cascade notation (..) allows performing multiple operations on the same object without repeating the object reference. Instead of calling button.color = red; button.text = 'Hi'; you write button..color = red..text = 'Hi'. The null-aware cascade (?...) works with nullable objects. Cascades return the original object, enabling method chaining."
        },
        {
            "instruction": "What is a Future in Dart?",
            "input": "",
            "output": "Future represents a value that will be available at some point in the future. It is the primary tool for asynchronous programming. A Future is either incomplete (waiting for a result) or completed (with a value or error). Use async/await or then/catchError to handle results. Future.wait runs multiple futures in parallel. Future.delayed creates a delayed computation."
        },
        {
            "instruction": "What is async and await in Dart?",
            "input": "",
            "output": "async marks a function as asynchronous, allowing it to use await. await pauses execution until a Future completes and returns its value. The function continues after the Future resolves. async functions always return a Future. Error handling uses try-catch around await statements. Multiple independent futures can run concurrently with Future.wait or parallel await."
        },
        {
            "instruction": "What is the Completer class in Dart?",
            "input": "",
            "output": "Completer creates a Future that can be completed manually at a later time. Use Completer<T>() to create one, access future via completer.future, complete with completer.complete(value) or completer.completeError(error). It bridges callback-based APIs and Future-based code. It should only be completed once — completing again throws a StateError."
        },
        {
            "instruction": "What are named constructors in Dart?",
            "input": "",
            "output": "Named constructors provide alternative constructors with descriptive names: Point.origin() : x = 0, y = 0. They allow multiple constructors for a class, each with a different name and initialization logic. Dart does not support constructor overloading by parameter type, so named constructors serve this purpose. Common examples: fromJson, fromMap, empty."
        },
        {
            "instruction": "What is the super keyword in Dart?",
            "input": "",
            "output": "super refers to the parent class instance. It is used to call parent constructors (super.namedConstructor()), access parent methods (super.method()), and parent fields. In constructor initializer lists, super() calls the parent constructor. Dart 2.17+ supports super parameters: MyClass(super.name) passes name directly to the parent constructor, reducing boilerplate."
        },
        {
            "instruction": "What is the this keyword in Dart?",
            "input": "",
            "output": "this refers to the current instance of the class. It is used to disambiguate between member variables and parameters with the same name, and for constructor initialization shorthand: MyClass(this.name, this.age) automatically assigns constructor parameters to fields. It can also be used to call other constructors: this.named()."
        },
        {
            "instruction": "What is the Expanded widget in Flutter?",
            "input": "",
            "output": "Expanded is a widget used inside Row, Column, or Flex that expands its child to fill the remaining available space. It takes a flex factor (default 1) that determines how much space it gets relative to other Expanded children. Expanded(flex: 2) gets twice the space of Expanded(flex: 1). It is shorthand for Flexible with FlexFit.tight."
        },
        {
            "instruction": "What is the SingleChildScrollView widget in Flutter?",
            "input": "",
            "output": "SingleChildScrollView wraps a single child widget (typically a Column) and makes it scrollable when its content overflows the available space. It renders all content at once, so it is best for short content. Use the reverse property to scroll from the bottom. It supports both vertical and horizontal scrolling via scrollDirection."
        },
        {
            "instruction": "What is the difference between AppBar and SliverAppBar?",
            "input": "",
            "output": "AppBar is a fixed-height Material app bar used in Scaffold's appBar property. SliverAppBar is used inside CustomScrollView and supports scrolling effects: floating (reappears on scroll up), pinned (stays visible), snap (snaps open/closed), expandedHeight (expanded size), and flexibleSpace for collapsible content. SliverAppBar enables parallax scrolling effects."
        },
        {
            "instruction": "What is the AnimatedContainer widget in Flutter?",
            "input": "",
            "output": "AnimatedContainer automatically animates changes to its properties over a specified duration. When you update its color, width, height, padding, margin, decoration, or alignment, it smoothly transitions between the old and new values. It uses an implicit animation — just change the properties and the widget handles the animation automatically."
        },
        {
            "instruction": "What is the AnimatedOpacity widget in Flutter?",
            "input": "",
            "output": "AnimatedOpacity smoothly animates opacity changes on its child. When the opacity property changes, the widget transitions between the old and new values over the specified duration. It is simpler than manually controlling an AnimationController for opacity. Use it for fade-in/fade-out effects, showing/hiding elements, and visual transitions."
        },
        {
            "instruction": "What is the Image widget in Flutter?",
            "input": "",
            "output": "Image displays images from various sources: Image.asset (bundled assets), Image.network (URLs), Image.file (device files), Image.memory (byte data). Key properties: fit (BoxFit for sizing), width/height, filterQuality, color/colorBlendMode for tinting. Network images support loadingBuilder and errorBuilder for handling loading states and errors."
        },
        {
            "instruction": "What is the CachedNetworkImage widget in Flutter?",
            "input": "",
            "output": "CachedNetworkImage from the cached_network_image package downloads and caches network images to disk. It provides placeholder (shown during loading), errorWidget (shown on failure), and smooth fade-in transition. It significantly improves performance and user experience for apps displaying many network images by avoiding redundant downloads."
        },
        {
            "instruction": "What is the difference between hot reload and full restart?",
            "input": "",
            "output": "Hot reload injects updated source code into the running Dart VM while preserving app state in about one second. Full restart terminates the app process completely and starts fresh — cleaning all state and reinitializing everything from main(). Full restart is needed when changing native code, pubspec.yaml, or platform configuration. Hot reload works for most Dart code changes."
        },
        {
            "instruction": "What is the SizedBox widget in Flutter?",
            "input": "",
            "output": "SizedBox constrains its child to a specific width and height. It is commonly used for adding fixed spacing: SizedBox(height: 16) between items in a Column, SizedBox(width: 8) between items in a Row. SizedBox.expand fills all available space. SizedBox.shrink takes minimum space. It is more efficient than Container for simple sizing."
        },
        {
            "instruction": "What is the difference between Navigator.push and Navigator.pushNamed?",
            "input": "",
            "output": "Navigator.push takes a Route object directly: Navigator.push(context, MaterialPageRoute(builder: (_) => Page())). Navigator.pushNamed takes a string route name: Navigator.pushNamed(context, '/page'). Named routes are defined in MaterialApp's routes map. pushNamed is cleaner for simple navigation but push allows passing complex arguments. pushNamed works with onGenerateRoute for dynamic routing."
        },
        {
            "instruction": "What is the Navigator.pushReplacement method?",
            "input": "",
            "output": "Navigator.pushReplacement replaces the current route with a new one, so pressing back does not return to the replaced page. It is commonly used for login-to-home navigation (so users cannot go back to login) and splash-to-home transitions. pushReplacementNamed is the named route variant. pushAndRemoveUntil removes all previous routes below the new one."
        },
        {
            "instruction": "What is the Dart const constructor?",
            "input": "",
            "output": "A const constructor creates compile-time constant objects. All fields must be final. Instances created with const keyword are canonicalized — identical const objects share the same memory. In Flutter, const constructors optimize performance by allowing the framework to skip rebuilding unchanged const widgets. Use const for immutable widgets and values wherever possible."
        },
        # ─── More Basic Questions (Batch 5) ─────────────────────────────────
        {
            "instruction": "What is the Dart null safety feature?",
            "input": "",
            "output": "Null safety means types are non-nullable by default. String name cannot be null. Use String? for nullable types. The ! operator asserts non-null. The ?. operator safely accesses nullable members. The ?? operator provides a default: name ?? 'Unknown'. Late keyword delays initialization: late String name. Null safety eliminates null reference errors at compile time."
        },
        {
            "instruction": "What is the difference between var, final, and const in Dart?",
            "input": "",
            "output": "var declares a mutable variable with inferred type. final is assigned once at runtime and cannot be reassigned. const is a compile-time constant — its value must be known at compile time. Final variables can hold runtime-computed values, const cannot. Prefer const for values known at compile time, final for values set once at runtime, and var only when reassignment is needed."
        },
        {
            "instruction": "What is the MaterialApp widget?",
            "input": "",
            "output": "MaterialApp is the root widget for Material Design apps. It configures theme, navigation, localization, and app-wide settings. Key properties: home (root widget), theme/darkTheme (styling), routes (named routes), navigatorKey, debugShowCheckedModeBanner. It wraps the app with Navigator, Theme, and MediaQuery inherited widgets. CupertinoApp is the iOS equivalent."
        },
        {
            "instruction": "How do you add a border to a Container in Flutter?",
            "input": "",
            "output": "Add borders via BoxDecoration in Container's decoration property: Container(decoration: BoxDecoration(border: Border.all(color: Colors.black, width: 2), borderRadius: BorderRadius.circular(8))). For specific sides: Border(top: BorderSide(color: Colors.red), bottom: BorderSide(color: Colors.blue)). Use shape: BoxShape.circle with border for circular borders."
        },
        {
            "instruction": "What is the Expanded widget in Flutter?",
            "input": "",
            "output": "Expanded expands a child of Row, Column, or Flex to fill available space along the main axis. It wraps a widget and gives it a flex factor (default 1). Multiple Expanded children share space proportionally based on flex values. Expanded is equivalent to Flexible with fit: FlexFit.tight. The child must be in a Row, Column, or Flex."
        },
        {
            "instruction": "What is the Flexible widget?",
            "input": "",
            "output": "Flexible allows a child of Row, Column, or Flex to share available space. Unlike Expanded, Flexible with FlexFit.loose lets the child take only the space it needs, up to its flex proportion. Flexible(flex: 2, fit: FlexFit.loose, child: widget). Expanded is a shorthand for Flexible(fit: FlexFit.tight)."
        },
        {
            "instruction": "How do you display a list of items in Flutter?",
            "input": "",
            "output": "Use ListView for vertical scrollable lists. ListView(children: [...]) for few items. ListView.builder(itemCount: items.length, itemBuilder: (ctx, i) => ListTile(title: Text(items[i]))) for large lists — it creates items lazily. ListView.separated adds separators between items. ListView.custom for custom child management."
        },
        {
            "instruction": "What is a Future in Dart?",
            "input": "",
            "output": "A Future represents a value that will be available asynchronously. It completes with a value (Future<T>) or an error. Use async/await: final result = await fetchData(). Or chain with .then() and .catchError(). Future.delayed creates a timed Future. Future.wait runs multiple Futures in parallel. Futures are single-value — for multiple values, use Streams."
        },
        {
            "instruction": "What is a Stream in Dart?",
            "input": "",
            "output": "A Stream is a sequence of asynchronous events. Unlike Future (single value), Stream delivers multiple values over time. Listen with stream.listen(onData). Use StreamBuilder in Flutter for reactive UI. StreamController creates streams manually. Types: single-subscription (one listener) and broadcast (multiple listeners). Common operators: map, where, distinct, take, skip."
        },
        {
            "instruction": "How do you navigate between screens in Flutter?",
            "input": "",
            "output": "Navigation uses Navigator: Navigator.push(context, MaterialPageRoute(builder: (_) => SecondScreen())) to push a new screen. Navigator.pop(context) to go back. Named routes: Navigator.pushNamed(context, '/second'). Pass data via constructor parameters or route arguments. GoRouter package provides declarative, URL-based routing with deep linking support."
        },
        {
            "instruction": "What is the setState method?",
            "input": "",
            "output": "setState is a method on StatefulWidget's State class that triggers a rebuild. When you change state variables, wrap the change in setState(() { counter++; }). This marks the widget as dirty and schedules a rebuild. Never call setState after dispose. Avoid heavy computation inside setState — compute first, then update state."
        },
        {
            "instruction": "What is the BuildContext in Flutter?",
            "input": "",
            "output": "BuildContext represents a widget's location in the widget tree. It is used to access inherited widgets like Theme.of(context), MediaQuery.of(context), and Navigator.of(context). Each widget has its own BuildContext. It is passed to the build method. Do not store BuildContext across async gaps as the widget may no longer be mounted."
        },
        {
            "instruction": "How do you handle user input with TextField?",
            "input": "",
            "output": "TextField captures text input. Use TextEditingController to read/set text: controller.text. Or use onChanged callback for real-time changes. Customize with decoration: InputDecoration(labelText: 'Name', border: OutlineInputBorder()). Use keyboardType for input type (text, number, email). obscureText: true for password fields. Dispose the controller in dispose()."
        },
        {
            "instruction": "What is the Scaffold widget?",
            "input": "",
            "output": "Scaffold provides the basic Material Design visual structure. It contains appBar (top bar), body (main content), floatingActionButton, drawer (side menu), bottomNavigationBar, and bottomSheet. It handles the layout of these components automatically. Most screens use Scaffold as their root layout widget."
        },
        {
            "instruction": "How do you show a SnackBar in Flutter?",
            "input": "",
            "output": "Show a SnackBar with ScaffoldMessenger: ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Message'), action: SnackBarAction(label: 'Undo', onPressed: () {}), duration: Duration(seconds: 3))). SnackBars appear at the bottom of the screen and auto-dismiss. ScaffoldMessenger.of(context).hideCurrentSnackBar() to dismiss manually."
        },
        {
            "instruction": "What is a GlobalKey in Flutter?",
            "input": "",
            "output": "GlobalKey uniquely identifies a widget across the entire app. It provides access to the widget's State and RenderObject: globalKey.currentState, globalKey.currentContext. Used for: accessing Form state (formKey.currentState!.validate()), controlling AnimatedList, RepaintBoundary capture. GlobalKeys are expensive — only use when necessary. Prefer ValueKey or ObjectKey for list items."
        },
        {
            "instruction": "How do you add images in Flutter?",
            "input": "",
            "output": "Display images with the Image widget. Asset images: Image.asset('assets/photo.png') after declaring in pubspec.yaml under flutter: assets:. Network images: Image.network('https://example.com/photo.jpg'). File images: Image.file(File(path)). Memory images: Image.memory(bytes). Control fitting with fit property: BoxFit.cover, contain, fill. Use width and height for sizing."
        },
        {
            "instruction": "What are keys in Flutter and when to use them?",
            "input": "",
            "output": "Keys identify widgets across builds, preserving state correctly. Without keys, Flutter matches widgets by position. ValueKey uses a value (id) for identity. ObjectKey uses an object reference. UniqueKey creates a unique identity each time. GlobalKey provides cross-tree identity. Use keys in lists, when reordering widgets, or when widget type is the same but identity differs."
        },
        {
            "instruction": "How do you create a button in Flutter?",
            "input": "",
            "output": "Flutter provides several button types: ElevatedButton(onPressed: () {}, child: Text('Click')) for raised buttons, TextButton for flat text buttons, OutlinedButton for bordered buttons, IconButton for icon-only buttons, FloatingActionButton for FABs. Style with styleFrom: ElevatedButton.styleFrom(backgroundColor: Colors.blue). All buttons require onPressed callback — null makes them disabled."
        },
        {
            "instruction": "What is the Dart Map data structure?",
            "input": "",
            "output": "Map is a collection of key-value pairs. Create with literal: Map<String, int> ages = {'Alice': 30, 'Bob': 25}. Access: ages['Alice']. Add: ages['Carol'] = 28. Check: ages.containsKey('Alice'). Iterate: ages.forEach((key, value) { ... }) or entries. Methods: keys, values, length, remove('key'), putIfAbsent, update. Maps are unordered by default."
        },
        {
            "instruction": "What is the Dart List data structure?",
            "input": "",
            "output": "List is an ordered collection. Create: List<int> nums = [1, 2, 3]. Access by index: nums[0]. Methods: add, addAll, insert, remove, removeAt, contains, indexOf, sort, reversed, sublist, length, isEmpty. Growable by default. Fixed-length: List.filled(3, 0). List comprehension: [for (var i in items) i.name]. Spread: [...list1, ...list2]."
        },
        {
            "instruction": "How do you handle errors in Dart?",
            "input": "",
            "output": "Use try-catch-finally: try { result = riskyOperation(); } catch (e, stackTrace) { print('Error: $e'); } finally { cleanup(); }. Catch specific types: on FormatException catch (e) { ... }. Throw exceptions: throw Exception('message'). Create custom exceptions: class MyException implements Exception { final String msg; MyException(this.msg); }. Use rethrow to re-throw caught exceptions."
        },
        {
            "instruction": "What is the ClipRRect widget?",
            "input": "",
            "output": "ClipRRect clips its child with a rounded rectangle. ClipRRect(borderRadius: BorderRadius.circular(16), child: Image.network(url)). Used to create rounded images, containers, and cards. Unlike Container's borderRadius which only applies to decoration, ClipRRect actually clips the child widget. ClipOval clips to an oval/circle shape. ClipPath clips to custom paths."
        },
        {
            "instruction": "What is the FutureBuilder widget?",
            "input": "",
            "output": "FutureBuilder builds UI based on a Future's state. FutureBuilder<String>(future: fetchData(), builder: (context, snapshot) { if (snapshot.connectionState == ConnectionState.waiting) return CircularProgressIndicator(); if (snapshot.hasError) return Text('Error'); return Text(snapshot.data!); }). It handles loading, error, and data states. Avoid creating the Future inside build — it would restart on every rebuild."
        },
        {
            "instruction": "What is the StreamBuilder widget?",
            "input": "",
            "output": "StreamBuilder rebuilds UI whenever a Stream emits data. StreamBuilder<int>(stream: counterStream, builder: (context, snapshot) { if (!snapshot.hasData) return Text('Waiting...'); return Text('Count: ${snapshot.data}'); }). It listens to the stream automatically and disposes on widget disposal. Handles connectionState: none, waiting, active, done. Use for real-time data like chat messages, live data."
        },
        {
            "instruction": "How do you add spacing between widgets in Flutter?",
            "input": "",
            "output": "Spacing methods: SizedBox(height: 16) or SizedBox(width: 16) between widgets. Padding(padding: EdgeInsets.all(8), child: widget) for internal spacing. EdgeInsets.symmetric, .only for specific sides. In Row/Column, use MainAxisAlignment.spaceBetween or spaceEvenly for even distribution. Gap(16) from the gap package is a modern alternative to SizedBox for spacing."
        },
        {
            "instruction": "What is the AnimatedContainer widget?",
            "input": "",
            "output": "AnimatedContainer automatically animates changes to its properties: width, height, color, padding, margin, decoration, alignment. Specify duration and curve: AnimatedContainer(duration: Duration(milliseconds: 300), curve: Curves.easeInOut, width: isExpanded ? 200 : 100, color: isActive ? Colors.blue : Colors.grey). No AnimationController needed — just change properties and it animates."
        },
        {
            "instruction": "What is the Wrap widget in Flutter?",
            "input": "",
            "output": "Wrap lays out children in multiple rows or columns, wrapping to the next line when space runs out. Unlike Row (which overflows) or Column, Wrap handles overflow gracefully. Properties: direction (horizontal/vertical), spacing (gap between children), runSpacing (gap between lines), alignment, crossAxisAlignment. Used for tags, chips, buttons that should flow to the next line."
        },
        {
            "instruction": "How do you create a dropdown in Flutter?",
            "input": "",
            "output": "DropdownButton creates a dropdown selector: DropdownButton<String>(value: selectedValue, items: options.map((e) => DropdownMenuItem(value: e, child: Text(e))).toList(), onChanged: (value) { setState(() => selectedValue = value!); }). DropdownButtonFormField adds form validation support. Customize with style, icon, underline, and isExpanded properties."
        },
        {
            "instruction": "What is the SingleChildScrollView widget?",
            "input": "",
            "output": "SingleChildScrollView makes a single child scrollable when it exceeds available space. Wrap a Column in SingleChildScrollView to prevent overflow. Properties: scrollDirection, padding, controller, physics. Unlike ListView, it renders all children at once — suitable for small content. For large lists, use ListView.builder which lazily builds items."
        },
        {
            "instruction": "What is the SafeArea widget in Flutter?",
            "input": "",
            "output": "SafeArea adds padding to avoid system intrusions like the status bar, notch, and bottom navigation bar. It uses MediaQuery to determine safe insets. Wrap your screen content: SafeArea(child: Scaffold(body: content)). Control which edges to respect: SafeArea(top: true, bottom: false). Essential for modern devices with notches and rounded corners."
        },
        {
            "instruction": "How do you create a grid layout in Flutter?",
            "input": "",
            "output": "GridView creates a 2D scrollable grid. GridView.count(crossAxisCount: 2, children: [...]) for fixed column count. GridView.extent(maxCrossAxisExtent: 200) for max item width. GridView.builder(gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount: 3, crossAxisSpacing: 10, childAspectRatio: 1), itemBuilder: ...) for large lazy grids."
        },
        {
            "instruction": "What is the Dart async/await syntax?",
            "input": "",
            "output": "async/await simplifies asynchronous programming. Mark a function async to use await inside: Future<String> getData() async { final response = await http.get(url); return response.body; }. await pauses execution until the Future completes. async functions always return Future. Use try-catch for error handling. await Future.wait([f1, f2]) runs multiple Futures concurrently."
        },
        {
            "instruction": "What is the InkWell widget?",
            "input": "",
            "output": "InkWell adds a Material ink splash effect on tap. Wrap any widget: InkWell(onTap: () {}, borderRadius: BorderRadius.circular(8), splashColor: Colors.blue.withOpacity(0.3), child: customWidget). It requires a Material ancestor for the ink effect to render. InkResponse provides a circular splash. Use for custom tappable widgets that need Material feedback."
        },
        {
            "instruction": "What is the Divider widget?",
            "input": "",
            "output": "Divider draws a thin horizontal line. Divider(height: 20, thickness: 2, indent: 16, endIndent: 16, color: Colors.grey). Height is the total space including the line. VerticalDivider is the vertical equivalent for use in Rows. Both extend DecoratedBox. Used to separate sections in lists, forms, and content areas."
        },
        {
            "instruction": "How do you create a Tab layout in Flutter?",
            "input": "",
            "output": "Tab layout uses TabController, TabBar, and TabBarView. Wrap in DefaultTabController(length: 3, child: Scaffold(appBar: AppBar(bottom: TabBar(tabs: [Tab(text: 'Tab1'), Tab(text: 'Tab2'), Tab(text: 'Tab3')])), body: TabBarView(children: [Page1(), Page2(), Page3()]))). For programmatic control, create TabController with SingleTickerProviderStateMixin."
        },
        {
            "instruction": "What is the Dart spread operator?",
            "input": "",
            "output": "The spread operator (...) expands a collection into another. Lists: final all = [...list1, ...list2]. Maps: final merged = {...map1, ...map2}. Null-aware spread (...?) skips null: [...?nullableList]. Used in Flutter for conditional widget lists: Column(children: [...fixedWidgets, if (show) optionalWidget, ...moreWidgets]). It creates a new collection, not a reference."
        },
        {
            "instruction": "What is the Dart extension method?",
            "input": "",
            "output": "Extensions add methods to existing types without modifying them: extension StringExt on String { bool get isEmail => contains('@'); String capitalize() => '${this[0].toUpperCase()}${substring(1)}'; }. Usage: 'test@mail.com'.isEmail. Extensions can add methods, getters, setters, and operators. They are resolved statically at compile time, not dynamically."
        },
        {
            "instruction": "How do you use CustomScrollView in Flutter?",
            "input": "",
            "output": "CustomScrollView combines multiple scrollable areas using slivers. CustomScrollView(slivers: [SliverAppBar(floating: true), SliverGrid(...), SliverList(...)]). Each sliver handles its own scrolling portion. SliverToBoxAdapter wraps a non-sliver widget. SliverFillRemaining fills remaining space. It provides a single scroll position for the entire view, unlike nested ListViews."
        },
        {
            "instruction": "What is the difference between hot reload and hot restart?",
            "input": "",
            "output": "Hot reload injects updated source code into the running Dart VM, preserving app state. It takes seconds and is used for UI tweaks. Hot restart completely restarts the app, resetting all state. It takes longer but handles changes hot reload cannot: static field changes, main() changes, enum changes, generic type changes. Both are development-only features."
        },
        {
            "instruction": "What is the ThemeData class?",
            "input": "",
            "output": "ThemeData defines the visual theme for a MaterialApp. Key properties: colorScheme (primary, secondary, surface colors), textTheme (text styles), useMaterial3 (Material 3 design), brightness (light/dark), elevatedButtonTheme, inputDecorationTheme, cardTheme. Create with ThemeData(colorScheme: ColorScheme.fromSeed(seedColor: Colors.blue), useMaterial3: true). Access with Theme.of(context)."
        },
        {
            "instruction": "How do you add custom fonts in Flutter?",
            "input": "",
            "output": "Add font files (.ttf, .otf) to a fonts/ directory. Declare in pubspec.yaml under flutter: fonts: - family: Roboto fonts: - asset: fonts/Roboto-Regular.ttf - asset: fonts/Roboto-Bold.ttf weight: 700. Use in TextStyle: TextStyle(fontFamily: 'Roboto', fontWeight: FontWeight.bold). Apply globally in ThemeData's textTheme. Google Fonts package provides fonts without bundling."
        },
        {
            "instruction": "What is the Positioned widget?",
            "input": "",
            "output": "Positioned places a child within a Stack at specific coordinates. Positioned(top: 10, left: 20, child: widget). Properties: top, bottom, left, right, width, height. Positioned.fill fills the entire Stack. Positioned.directional supports RTL layouts. Only works as a direct child of Stack. Combine top+bottom or left+right to stretch the child."
        },
        {
            "instruction": "What is the Hero animation widget?",
            "input": "",
            "output": "Hero creates a shared element transition between two screens. Wrap the same widget on both screens with Hero and the same tag: Hero(tag: 'avatar', child: CircleAvatar(...)). When navigating, Flutter animates the widget flying from source to destination position. Tags must be unique per screen. Use flightShuttleBuilder for custom in-flight appearance."
        },
        {
            "instruction": "How do you handle form submission in Flutter?",
            "input": "",
            "output": "Forms use Form widget with GlobalKey<FormState>. Wrap TextFormFields in Form. Each field has a validator function. On submit: if (formKey.currentState!.validate()) { formKey.currentState!.save(); submitData(); }. The save() method triggers each field's onSaved callback. Use Form.of(context) for ancestor form access. AutovalidateMode controls when validation runs."
        },
        {
            "instruction": "What is the Opacity widget?",
            "input": "",
            "output": "Opacity controls a child's transparency: Opacity(opacity: 0.5, child: Image(...)). Values range from 0.0 (invisible) to 1.0 (fully visible). Opacity is expensive because it creates a separate layer for compositing. For simple show/hide, use Visibility widget instead. AnimatedOpacity provides smooth opacity transitions with a duration and curve."
        },
        {
            "instruction": "What is the Dart typedef keyword?",
            "input": "",
            "output": "typedef creates a type alias. For function types: typedef Compare = int Function(int a, int b). For any type: typedef StringList = List<String>. Usage: void sort(Compare compare) { ... }. Typedefs improve code readability by giving meaningful names to complex types. They are especially useful for callback function signatures and generic type aliases."
        },
        {
            "instruction": "How do you add a background color to a screen?",
            "input": "",
            "output": "Set Scaffold's backgroundColor: Scaffold(backgroundColor: Colors.grey[100], body: content). Or wrap the body in a Container with color or decoration: Container(decoration: BoxDecoration(gradient: LinearGradient(colors: [Colors.blue, Colors.purple]))). Theme-level: set scaffoldBackgroundColor in ThemeData for consistent background across all screens."
        },
        {
            "instruction": "What is the Dart cascade operator?",
            "input": "",
            "output": "The cascade operator (..) allows multiple operations on the same object without repeating the variable name. Example: var paint = Paint()..color = Colors.red..style = PaintingStyle.fill..strokeWidth = 2.0. Each .. returns the original object. Null-aware cascade (?..) works with nullable objects. Cascades are useful for configuring objects with many properties."
        },
        {
            "instruction": "What is pubspec.yaml in Flutter?",
            "input": "",
            "output": "pubspec.yaml is the project configuration file. It defines: name (project name), description, version, environment (SDK constraints), dependencies (pub packages), dev_dependencies (test/build tools), flutter section (assets, fonts, plugin settings). Run flutter pub get after adding dependencies. Use ^ for version ranges: ^2.0.0 means >=2.0.0 <3.0.0."
        },
        {
            "instruction": "What is the GestureDetector widget?",
            "input": "",
            "output": "GestureDetector detects touch gestures on its child. Supports: onTap, onDoubleTap, onLongPress, onPanUpdate (drag), onScaleUpdate (pinch), onVerticalDragUpdate, onHorizontalDragUpdate. GestureDetector(onTap: () => print('tapped'), child: Container(...)). It doesn't provide visual feedback — use InkWell for Material ripple effect. Gestures are disambiguated when multiple detectors compete."
        },
        {
            "instruction": "What is the difference between mainAxisAlignment and crossAxisAlignment?",
            "input": "",
            "output": "mainAxisAlignment controls child positioning along the primary axis (horizontal for Row, vertical for Column). crossAxisAlignment controls positioning along the perpendicular axis. mainAxisAlignment options: start, end, center, spaceBetween, spaceAround, spaceEvenly. crossAxisAlignment options: start, end, center, stretch, baseline. Default is start for both."
        },
        {
            "instruction": "What is a Future in Dart?",
            "input": "",
            "output": "A Future represents a value that will be available at some point in the future. It's Dart's way of handling asynchronous operations like network requests or file I/O. Use async/await or .then() to handle the result. Future<String> fetchData() async { return 'data'; }. Futures can complete with a value or an error. Use try/catch with await or .catchError() for error handling."
        },
        {
            "instruction": "What is the difference between TextButton, ElevatedButton, and OutlinedButton?",
            "input": "",
            "output": "TextButton is a flat button with no elevation or outline, used for less prominent actions. ElevatedButton has a raised appearance with shadow/elevation, used for primary actions. OutlinedButton has a border outline with no fill, used for secondary actions. All accept onPressed callback and child widget. Style with styleFrom(): ElevatedButton.styleFrom(backgroundColor: Colors.blue). All are Material 3 replacements for FlatButton, RaisedButton, and OutlineButton."
        },
        {
            "instruction": "How do you add images in Flutter?",
            "input": "",
            "output": "For asset images: add files to assets/ folder, declare in pubspec.yaml under flutter > assets, use Image.asset('assets/image.png'). For network images: Image.network('https://example.com/image.png'). Properties: width, height, fit (BoxFit.cover, contain, fill). Use DecorationImage in Container's BoxDecoration. For cached network images, use cached_network_image package. Use Image.file() for local file system images."
        },
        {
            "instruction": "What is the Opacity widget in Flutter?",
            "input": "",
            "output": "Opacity makes its child partially transparent. Opacity(opacity: 0.5, child: Text('Semi-transparent')). Value ranges from 0.0 (invisible) to 1.0 (fully visible). Note: Opacity is expensive as it requires an offscreen buffer. For simple cases, prefer using color with alpha: Color.fromRGBO(0, 0, 0, 0.5) or Colors.black54. AnimatedOpacity provides smooth transitions."
        },
        {
            "instruction": "What is the SizedBox widget?",
            "input": "",
            "output": "SizedBox constrains its child to a specific width and/or height. SizedBox(width: 100, height: 50, child: Container(...)). Common uses: adding fixed spacing between widgets (SizedBox(height: 16)), constraining child dimensions, SizedBox.expand() fills all available space, SizedBox.shrink() takes zero space. Often preferred over Container when only size constraint is needed since it's more lightweight."
        },
        {
            "instruction": "What is the Divider widget in Flutter?",
            "input": "",
            "output": "Divider creates a thin horizontal line. Divider(height: 20, thickness: 2, color: Colors.grey, indent: 16, endIndent: 16). height is the total space (not line thickness). Use VerticalDivider for vertical lines in Row widgets. Divider is a convenience widget wrapping Container with BoxDecoration."
        },
        {
            "instruction": "What is the CircularProgressIndicator in Flutter?",
            "input": "",
            "output": "CircularProgressIndicator shows loading state. Indeterminate: CircularProgressIndicator() — spins continuously. Determinate: CircularProgressIndicator(value: 0.7) — shows 70% progress. Customize: strokeWidth, backgroundColor, valueColor (AnimationController for color animation). Use LinearProgressIndicator for horizontal progress bars. Wrap in Center widget for proper positioning."
        },
        {
            "instruction": "What are keys in Flutter and why are they important?",
            "input": "",
            "output": "Keys help Flutter identify which widgets changed during rebuilds. Types: ValueKey (uses value for identity), ObjectKey (uses object reference), UniqueKey (always unique), GlobalKey (unique across entire app). Use keys in lists with reorderable items: ListView.builder(itemBuilder: (ctx, i) => ListTile(key: ValueKey(items[i].id), ...)). Without keys, Flutter matches by index which causes issues during reordering."
        },
        {
            "instruction": "What is the Spacer widget in Flutter?",
            "input": "",
            "output": "Spacer creates flexible space between widgets in Row, Column, or Flex. Row(children: [Text('Left'), Spacer(), Text('Right')]). Spacer(flex: 2) takes twice the space as Spacer(flex: 1). Under the hood, Spacer is an Expanded with an empty SizedBox. Use for pushing widgets to edges or distributing space proportionally."
        },
        {
            "instruction": "What is the AspectRatio widget?",
            "input": "",
            "output": "AspectRatio sizes its child to a specific width-to-height ratio. AspectRatio(aspectRatio: 16/9, child: Container(color: Colors.blue)). The child fills the largest area while maintaining the ratio. Common ratios: 16/9 (video), 4/3 (photo), 1 (square). Useful for videos, images, cards. Respects parent constraints — if parent is too narrow, height adjusts."
        },
        {
            "instruction": "What is the difference between Flexible and Expanded?",
            "input": "",
            "output": "Both distribute space in Row/Column. Expanded forces child to fill all remaining space (fit: FlexFit.tight). Flexible lets child be smaller than allocated space (fit: FlexFit.loose). Expanded(child: Container()) — container fills all available space. Flexible(child: Container()) — container can be smaller. Both accept flex parameter for proportional sizing: Expanded(flex: 2) takes twice the space of Expanded(flex: 1)."
        },
        {
            "instruction": "How do you create a Card widget in Flutter?",
            "input": "",
            "output": "Card is a Material design panel with elevation. Card(elevation: 4, shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)), margin: EdgeInsets.all(8), child: Padding(padding: EdgeInsets.all(16), child: Column(children: [Text('Title'), Text('Content')]))). Card inherits theme's cardColor. Use InkWell inside for tap effects. Card clips children based on clipBehavior. Material 3 cards: Card.filled(), Card.outlined()."
        },
        {
            "instruction": "What is the purpose of the SafeArea widget?",
            "input": "",
            "output": "SafeArea adds padding to avoid system UI intrusions like status bar, notch, navigation bar, and rounded corners. SafeArea(child: Scaffold(...)). Properties: top, bottom, left, right (booleans to control each side), minimum (minimum padding). Without SafeArea, content can be hidden behind the status bar or iPhone notch. Use inside Scaffold's body, not outside Scaffold."
        },
        {
            "instruction": "What is the WillPopScope widget used for?",
            "input": "",
            "output": "WillPopScope intercepts the back button press. WillPopScope(onWillPop: () async { final shouldLeave = await showDialog(context: context, builder: (_) => AlertDialog(title: Text('Exit?'), actions: [TextButton(onPressed: () => Navigator.pop(context, false), child: Text('No')), TextButton(onPressed: () => Navigator.pop(context, true), child: Text('Yes'))])); return shouldLeave ?? false; }, child: Scaffold(...)). Deprecated in newer Flutter — use PopScope instead. Return true to allow pop, false to prevent."
        },
    ]


def generate_intermediate_questions():
    """Generate intermediate-level Flutter Q&A pairs."""
    return [
        # Widget Lifecycle
        {
            "instruction": "Explain the lifecycle of a StatefulWidget in Flutter.",
            "input": "",
            "output": "The StatefulWidget lifecycle consists of several stages: createState() creates the State object, initState() initializes state (called once), didChangeDependencies() is called when dependencies change, build() renders the UI (can be called multiple times), didUpdateWidget() fires when parent rebuilds with new config, setState() triggers rebuilds, deactivate() temporarily removes the state, and dispose() permanently cleans up resources."
        },
        {
            "instruction": "What is the didChangeDependencies() method in Flutter?",
            "input": "",
            "output": "didChangeDependencies() is a lifecycle method called when the State object's dependencies change, such as when an InheritedWidget that this widget depends on updates. It is called after initState() and whenever an inherited dependency changes. It is safe to call BuildContext-dependent methods here, unlike in initState()."
        },
        {
            "instruction": "What is the didUpdateWidget() method in Flutter?",
            "input": "",
            "output": "didUpdateWidget() is called when the parent widget rebuilds and provides a new configuration (widget instance) to this State object. It receives the old widget as a parameter, allowing comparison between old and new configurations. It is useful for responding to property changes, such as updating animation controllers when duration changes."
        },
        {
            "instruction": "What is the deactivate() method in Flutter?",
            "input": "",
            "output": "deactivate() is called when the State object is removed from the widget tree, but it may be reinserted before the current frame ends. It is called before dispose() and is less commonly overridden. It is useful for removing references that depend on the widget's position in the tree, such as unregistering from ancestor widgets."
        },
        # Navigation
        {
            "instruction": "How does navigation work in Flutter?",
            "input": "",
            "output": "Flutter uses a Navigator widget that manages a stack of Route objects. You push new routes onto the stack to navigate forward (Navigator.push) and pop them to go back (Navigator.pop). Flutter supports imperative navigation (push/pop with MaterialPageRoute), named routes (pushNamed with a route map), and Navigator 2.0 (Router/RouterDelegate) for declarative, URL-based navigation."
        },
        {
            "instruction": "What is Navigator 2.0 in Flutter?",
            "input": "",
            "output": "Navigator 2.0 is Flutter's declarative navigation API introduced for better deep linking and web URL support. It uses a Router widget with a RouterDelegate and RouteInformationParser. Unlike the imperative push/pop approach, it allows the app to reactively build the navigation stack based on app state, making it better suited for web and complex navigation flows."
        },
        {
            "instruction": "How do you pass data between screens in Flutter?",
            "input": "",
            "output": "Data can be passed between screens in several ways: through constructor parameters when pushing a new route, via route arguments using Navigator.pushNamed with arguments parameter and ModalRoute.of(context).settings.arguments to retrieve them, by returning data with Navigator.pop(context, data) and awaiting the Future from Navigator.push, or through state management solutions."
        },
        {
            "instruction": "What is the GoRouter package in Flutter?",
            "input": "",
            "output": "GoRouter is a popular declarative routing package for Flutter that simplifies navigation with URL-based routing. It provides a configuration-based approach with GoRoute objects defining paths, builders, and redirects. It supports deep linking, nested navigation, named routes, path parameters, query parameters, and shell routes for persistent UI elements."
        },
        {
            "instruction": "What is a PageRouteBuilder in Flutter?",
            "input": "",
            "output": "PageRouteBuilder is a utility class for creating custom page route transitions. It takes a pageBuilder for the destination widget and a transitionsBuilder for defining custom animations. This allows you to create slide, fade, scale, or rotation transitions between screens without creating a full custom Route class."
        },
        # Layouts
        {
            "instruction": "What is the Flex widget in Flutter?",
            "input": "",
            "output": "Flex is the base class for Row and Column widgets. It arranges children along a single axis — horizontal or vertical — specified by the direction parameter. Row is simply Flex with Axis.horizontal and Column is Flex with Axis.vertical. Using Flex directly is useful when the layout direction needs to be determined dynamically at runtime."
        },
        {
            "instruction": "What is the ConstrainedBox widget in Flutter?",
            "input": "",
            "output": "ConstrainedBox imposes additional constraints on its child widget. It takes a BoxConstraints parameter that specifies minimum and maximum width and height. The resulting constraints are the intersection of the parent's constraints and the specified constraints. It is useful for setting minimum sizes or limiting maximum dimensions of flexible widgets."
        },
        {
            "instruction": "What is IntrinsicHeight in Flutter?",
            "input": "",
            "output": "IntrinsicHeight is a widget that sizes its child to the child's intrinsic height. It forces the child to have a height equal to the maximum intrinsic height of all its descendants. This is useful in Row layouts where children need to match the tallest child's height. However, it can be expensive as it measures the child tree twice."
        },
        {
            "instruction": "What is a CustomScrollView in Flutter?",
            "input": "",
            "output": "CustomScrollView is a scrollable widget that creates custom scroll effects using slivers. Unlike ListView or GridView, it allows combining different scroll behaviors — a SliverAppBar, SliverList, SliverGrid, and SliverToBoxAdapter — in a single scrollable area. It provides full control over the scroll physics and the arrangement of scrollable content."
        },
        {
            "instruction": "What are Slivers in Flutter?",
            "input": "",
            "output": "Slivers are scrollable areas that can be composed together in a CustomScrollView. They define a portion of the scrollable layout and lazily build their content as it scrolls into view. Common slivers include SliverList, SliverGrid, SliverAppBar, SliverPadding, and SliverToBoxAdapter. They enable advanced scrolling effects like collapsing headers and nested scroll views."
        },
        {
            "instruction": "What is the SliverAppBar widget in Flutter?",
            "input": "",
            "output": "SliverAppBar is a Material Design app bar that integrates with CustomScrollView to create collapsing, expanding, or floating header effects. It supports pinned (stays visible), floating (reappears on scroll up), and snap behavior. The flexibleSpace property allows adding content that expands/collapses with the app bar, commonly used with FlexibleSpaceBar."
        },
        {
            "instruction": "What is the difference between mainAxisSize.min and mainAxisSize.max?",
            "input": "",
            "output": "mainAxisSize controls how much space a Row or Column occupies along its main axis. MainAxisSize.max (default) makes the widget expand to fill all available space along the main axis. MainAxisSize.min makes the widget shrink to fit only its children's combined size. This is particularly useful when you want a Column or Row to wrap its content tightly."
        },
        # Forms
        {
            "instruction": "How do forms work in Flutter?",
            "input": "",
            "output": "Flutter forms use the Form widget with a GlobalKey<FormState> for validation and state management. Form wraps multiple TextFormField widgets, each with a validator callback. Calling formKey.currentState!.validate() triggers all validators and returns true if all pass. formKey.currentState!.save() triggers each field's onSaved callback to collect values."
        },
        {
            "instruction": "What is a TextFormField in Flutter?",
            "input": "",
            "output": "TextFormField is a TextField wrapped with FormField integration, providing built-in support for Form validation. It accepts a validator function that returns an error string or null, and an onSaved callback for collecting the value when the form is saved. It automatically displays validation errors below the field when validation fails."
        },
        {
            "instruction": "What is the TextEditingController in Flutter?",
            "input": "",
            "output": "TextEditingController is a controller for an editable text field that lets you read the current value, set the value programmatically, and listen for changes. It provides the text property for reading/setting the value and a selection property for cursor position. It should be disposed in the dispose() method to prevent memory leaks."
        },
        {
            "instruction": "What is the FocusNode in Flutter?",
            "input": "",
            "output": "FocusNode is an object that represents a node in the focus tree and manages keyboard focus for a widget. It can be used to request focus (focusNode.requestFocus()), unfocus (focusNode.unfocus()), and listen for focus changes. FocusNodes must be disposed in the dispose() method. They are commonly used with TextFields to control which field has keyboard focus."
        },
        # Animations
        {
            "instruction": "What are the types of animations in Flutter?",
            "input": "",
            "output": "Flutter supports two main types of animations: implicit animations and explicit animations. Implicit animations (AnimatedContainer, AnimatedOpacity, etc.) automatically animate when property values change. Explicit animations use AnimationController with vsync for fine-grained control, supporting Tween, CurvedAnimation, and custom animation builders for complex, coordinated animations."
        },
        {
            "instruction": "What is an AnimationController in Flutter?",
            "input": "",
            "output": "AnimationController is the core class for explicit animations in Flutter. It generates values from 0.0 to 1.0 over a specified duration and provides methods like forward(), reverse(), repeat(), and stop(). It requires a TickerProvider (vsync) and must be disposed. It can be combined with Tweens and Curves for custom value ranges and easing."
        },
        {
            "instruction": "What is a Tween in Flutter?",
            "input": "",
            "output": "A Tween defines a mapping between a beginning and ending value for an animation. It takes a begin and end value and provides an animate() method that creates an Animation bound to an AnimationController. Tweens can interpolate various types: numbers (Tween<double>), colors (ColorTween), sizes (SizeTween), and even custom types with a lerp function."
        },
        {
            "instruction": "What is the TickerProvider mixin in Flutter?",
            "input": "",
            "output": "TickerProvider is a mixin that provides Ticker objects, which fire callbacks once per frame. AnimationController requires a vsync parameter of type TickerProvider to drive its animation. The SingleTickerProviderStateMixin is used when a State has one AnimationController, and TickerProviderStateMixin when multiple controllers are needed."
        },
        {
            "instruction": "What is the Hero widget in Flutter?",
            "input": "",
            "output": "Hero is a widget that creates a flying animation of a widget between two screens during navigation transitions. It requires a matching tag property on both the source and destination Hero widgets. When the route changes, Flutter automatically animates the Hero's child between its positions on the two screens, creating a smooth shared element transition."
        },
        {
            "instruction": "What is the AnimatedBuilder widget in Flutter?",
            "input": "",
            "output": "AnimatedBuilder is a widget that rebuilds when an Animation changes value. It takes an animation (Listenable) and a builder function, separating the animation logic from the widget tree. This is more efficient than using setState because only the subtree returned by the builder is rebuilt. It is the recommended approach for explicit animations."
        },
        {
            "instruction": "What are implicit animations in Flutter?",
            "input": "",
            "output": "Implicit animations are pre-built animated widgets that automatically animate when their properties change. They include AnimatedContainer, AnimatedOpacity, AnimatedPadding, AnimatedPositioned, AnimatedCrossFade, and AnimatedDefaultTextStyle. They require only a duration and optional curve parameter, handling all animation logic internally. They are the simplest way to add animations."
        },
        {
            "instruction": "What is the AnimatedOpacity widget?",
            "input": "",
            "output": "AnimatedOpacity is an implicit animation widget that smoothly transitions the opacity of its child when the opacity value changes. It takes an opacity value (0.0 to 1.0), a duration for the animation, and an optional curve. It is a simpler alternative to FadeTransition for basic fade animations without needing an AnimationController."
        },
        {
            "instruction": "What is a CurvedAnimation in Flutter?",
            "input": "",
            "output": "CurvedAnimation applies a non-linear curve to an Animation, modifying how the animation progresses over time. Instead of linear interpolation, it can ease in, ease out, bounce, or follow other mathematical curves. Flutter provides many built-in curves like Curves.easeInOut, Curves.bounceIn, and Curves.elasticOut. It wraps an AnimationController and is passed to Tweens."
        },
        # State Management & Architecture
        {
            "instruction": "What is state management in Flutter?",
            "input": "",
            "output": "State management refers to how you store, access, and update the application's data across widgets. Flutter offers multiple approaches: setState for local widget state, InheritedWidget for passing data down the tree, Provider for dependency injection and reactive state, Bloc for event-driven state with streams, Riverpod for compile-safe state management, and GetX for simplified reactive state."
        },
        {
            "instruction": "What is the Provider package in Flutter?",
            "input": "",
            "output": "Provider is a popular state management package that wraps InheritedWidget to make it easier to use. It provides various Provider types: Provider for immutable values, ChangeNotifierProvider for mutable state with notifications, FutureProvider and StreamProvider for async data, and MultiProvider for combining multiple providers. It uses context.read() and context.watch() for access."
        },
        {
            "instruction": "What is ChangeNotifier in Flutter?",
            "input": "",
            "output": "ChangeNotifier is a class that implements the Listenable interface and notifies listeners when data changes via notifyListeners(). It is commonly used as a base class for view models or state objects in the Provider pattern. When notifyListeners() is called, all widgets watching the ChangeNotifier are rebuilt to reflect the new state."
        },
        {
            "instruction": "What is the InheritedWidget in Flutter?",
            "input": "",
            "output": "InheritedWidget is a base class for widgets that efficiently propagate data down the widget tree. Descendant widgets can access the inherited data using the of(context) pattern. When the inherited data changes, only widgets that depend on it are rebuilt. Theme, MediaQuery, and Navigator are examples of InheritedWidgets. It forms the foundation for state management solutions like Provider."
        },
        {
            "instruction": "What is the ValueNotifier in Flutter?",
            "input": "",
            "output": "ValueNotifier is a ChangeNotifier that holds a single value and notifies listeners when the value changes. It is simpler than creating a full ChangeNotifier subclass when you only need to track one value. Combined with ValueListenableBuilder, it provides a lightweight way to rebuild widgets reactively without a state management package."
        },
        {
            "instruction": "What is the Consumer widget in Provider?",
            "input": "",
            "output": "Consumer is a Provider widget that accesses a provided object and rebuilds when it changes. Unlike context.watch(), Consumer can limit rebuilds to a specific subtree of the widget tree, improving performance. It takes a builder function with (context, value, child) parameters, where child is an optional non-rebuilding part of the subtree."
        },
        {
            "instruction": "What is the difference between context.read() and context.watch() in Provider?",
            "input": "",
            "output": "context.watch() retrieves a value from Provider and subscribes to changes — the widget rebuilds when the value updates. context.read() retrieves the value once without subscribing to changes — the widget does not rebuild on updates. Use watch() in build methods for reactive UI, and read() in callbacks like onPressed where you need the current value without rebuilding."
        },
        # HTTP & Networking
        {
            "instruction": "How do you make HTTP requests in Flutter?",
            "input": "",
            "output": "Flutter makes HTTP requests using the http package or dio package. With the http package, you import it and use http.get(), http.post(), http.put(), and http.delete() methods that return Futures. The response body is a string that you parse with jsonDecode(). Dio offers interceptors, form data, cancellation, and automatic JSON parsing."
        },
        {
            "instruction": "What is the dio package in Flutter?",
            "input": "",
            "output": "Dio is a powerful HTTP networking package for Flutter that provides interceptors, request cancellation, form data support, file downloading, timeout configuration, and automatic response transformation. It offers a more feature-rich alternative to the standard http package, with built-in support for retry logic, logging interceptors, and global configuration."
        },
        {
            "instruction": "How do you parse JSON in Flutter?",
            "input": "",
            "output": "JSON in Flutter is parsed using dart:convert's jsonDecode() function, which converts a JSON string into a Map or List. For type-safe parsing, you create model classes with fromJson() factory constructors and toJson() methods. The json_serializable package can auto-generate this boilerplate code using code generation with build_runner."
        },
        {
            "instruction": "What is the FutureBuilder widget in Flutter?",
            "input": "",
            "output": "FutureBuilder is a widget that builds itself based on the latest snapshot of a Future. It takes a future and a builder function that receives the AsyncSnapshot containing the connection state, data, and error. It handles loading (ConnectionState.waiting), error, and success states, making it ideal for displaying async data from API calls or database queries."
        },
        {
            "instruction": "What is the StreamBuilder widget in Flutter?",
            "input": "",
            "output": "StreamBuilder is a widget that rebuilds when a Stream emits new data. Like FutureBuilder, it provides an AsyncSnapshot in its builder function with connection state, data, and error. It is used for real-time data updates like chat messages, WebSocket data, Firestore snapshots, and any continuously changing data source."
        },
        # Storage & Persistence
        {
            "instruction": "How do you store data locally in Flutter?",
            "input": "",
            "output": "Flutter offers several local storage options: SharedPreferences for key-value pairs (settings, flags), sqflite for SQLite databases (structured relational data), Hive for NoSQL box-based storage (fast, lightweight), path_provider for file system access, and secure_storage for encrypted data. The choice depends on data complexity, size, and security requirements."
        },
        {
            "instruction": "What is the SharedPreferences package in Flutter?",
            "input": "",
            "output": "SharedPreferences is a Flutter plugin for persistent key-value storage using the platform's native shared preferences (NSUserDefaults on iOS, SharedPreferences on Android). It supports storing int, double, bool, String, and List<String>. It is suitable for simple data like user settings, flags, and small cached values. It is not suitable for large or complex data."
        },
        {
            "instruction": "What is the sqflite package in Flutter?",
            "input": "",
            "output": "sqflite is a Flutter plugin for SQLite database operations. It provides full SQL support for creating tables, inserting, querying, updating, and deleting records. It supports transactions, batches, and raw SQL queries. It is suitable for structured relational data that needs complex querying. The database file persists across app launches."
        },
        # Platform-Specific
        {
            "instruction": "What are platform channels in Flutter?",
            "input": "",
            "output": "Platform channels are Flutter's mechanism for communicating between Dart code and platform-native code (Java/Kotlin for Android, Swift/Objective-C for iOS). They use message passing with MethodChannel for method calls, EventChannel for event streams, and BasicMessageChannel for simple messages. This enables accessing platform-specific APIs not available through Dart."
        },
        {
            "instruction": "What is a MethodChannel in Flutter?",
            "input": "",
            "output": "MethodChannel is a platform channel type used for invoking named methods across the Dart-to-native boundary. The Dart side calls invokeMethod() with a method name and arguments, and the native side handles the call and returns a result. It uses standardized codecs for serialization and supports asynchronous communication via Futures."
        },
        # Testing
        {
            "instruction": "What are the types of testing in Flutter?",
            "input": "",
            "output": "Flutter supports three levels of testing: unit tests for testing individual functions, methods, and classes; widget tests for testing individual widgets in isolation with simulated interactions; and integration tests for testing complete app flows on a real device or emulator. Flutter provides the flutter_test package with testWidgets, pumpWidget, and finder utilities."
        },
        {
            "instruction": "What is a widget test in Flutter?",
            "input": "",
            "output": "A widget test verifies a single widget's behavior in isolation. It uses WidgetTester to pump widgets, simulate user interactions (tap, drag, enter text), and verify outcomes using Finder and Matcher. Widget tests run faster than integration tests because they don't require a real device. They test rendering, gesture handling, and state changes."
        },
        {
            "instruction": "What is the pump() method in widget testing?",
            "input": "",
            "output": "pump() is a method on WidgetTester that triggers a frame rebuild and processes pending microtasks. After performing actions like tapping or changing state, you call pump() to process the resulting build. pumpAndSettle() repeatedly calls pump() until there are no pending frames, which is useful for animations. Initial widget rendering uses pumpWidget()."
        },
        # Responsive Design
        {
            "instruction": "How do you build responsive UIs in Flutter?",
            "input": "",
            "output": "Responsive UIs in Flutter are built using MediaQuery for screen dimensions and device info, LayoutBuilder for parent constraints, the Flexible and Expanded widgets for proportional sizing, OrientationBuilder for orientation changes, and adaptive packages like flutter_screenutil. You can also use custom breakpoints to switch between mobile, tablet, and desktop layouts."
        },
        {
            "instruction": "What is OrientationBuilder in Flutter?",
            "input": "",
            "output": "OrientationBuilder is a widget that rebuilds when the device orientation changes between portrait and landscape. Its builder function receives the current Orientation, allowing you to return different widget trees for each orientation. It is simpler than using MediaQuery for orientation-based layouts and handles the rebuild logic automatically."
        },
        # Error Handling
        {
            "instruction": "How do you handle errors in Flutter?",
            "input": "",
            "output": "Flutter errors are handled through try-catch blocks for synchronous errors, .catchError() or try-catch with await for async errors, and FlutterError.onError for catching framework errors during widget building. For unhandled async errors, runZonedGuarded wraps the app to catch all uncaught exceptions. ErrorWidget.builder customizes the error display shown to users."
        },
        {
            "instruction": "What is the ErrorWidget in Flutter?",
            "input": "",
            "output": "ErrorWidget is the widget displayed when a build method throws an error. By default, it shows a red error screen in debug mode. You can customize it by setting ErrorWidget.builder to return a user-friendly widget in production. This prevents the app from showing technical error details to users while still logging the error."
        },
        # Internationalization
        {
            "instruction": "How do you implement internationalization (i18n) in Flutter?",
            "input": "",
            "output": "Flutter supports internationalization through the flutter_localizations package and the intl package. You define localized strings in ARB (Application Resource Bundle) files, configure supported locales in MaterialApp, and use the gen_l10n tool to generate type-safe localization classes. Labels are then accessed via AppLocalizations.of(context)!.someString within widgets."
        },
        # Advanced Widgets
        {
            "instruction": "What is the CustomPaint widget in Flutter?",
            "input": "",
            "output": "CustomPaint is a widget that provides a canvas for custom drawing. It takes a CustomPainter object that implements the paint() method using Canvas APIs for drawing shapes, lines, paths, text, and images. It also takes a shouldRepaint() method to optimize repaints. CustomPaint is used for charts, graphs, custom UI elements, and game graphics."
        },
        {
            "instruction": "What is the Transform widget in Flutter?",
            "input": "",
            "output": "Transform is a widget that applies a matrix transformation to its child before painting. It supports rotation (Transform.rotate), scaling (Transform.scale), and translation (Transform.translate) using Matrix4. The transformation only affects painting — the original layout space is preserved. It is commonly used for visual effects and custom animations."
        },
        {
            "instruction": "What is the RepaintBoundary widget in Flutter?",
            "input": "",
            "output": "RepaintBoundary creates a separate display list layer for its child, isolating it from repaints of surrounding widgets. When a widget frequently repaints (like animations), wrapping it in RepaintBoundary prevents the repaint from affecting the rest of the UI. This optimization is especially useful for complex UIs with localized animations or frequently updating widgets."
        },
        {
            "instruction": "What is the IndexedStack widget in Flutter?",
            "input": "",
            "output": "IndexedStack is a Stack that shows only one child at a time based on an index. Unlike showing/hiding widgets with Visibility, IndexedStack keeps all children in the widget tree but only displays the one at the specified index. This preserves the state of all children, making it useful for tab-based navigation where each tab should maintain its state."
        },
        {
            "instruction": "What is the PageView widget in Flutter?",
            "input": "",
            "output": "PageView is a scrollable widget that works page by page, snapping to each page. It can scroll horizontally or vertically and uses a PageController for programmatic control. PageView.builder provides lazy construction for performance. It is commonly used for onboarding screens, image carousels, and swipeable card interfaces."
        },
        {
            "instruction": "What is a GlobalKey in Flutter?",
            "input": "",
            "output": "GlobalKey is a key that is unique across the entire app. It allows accessing a widget's State, Element, or RenderObject from anywhere in the widget tree. GlobalKey<FormState> is commonly used for form validation. However, GlobalKeys are expensive and should be used sparingly — prefer passing state through constructors or state management solutions."
        },
        {
            "instruction": "What is the Dismissible widget in Flutter?",
            "input": "",
            "output": "Dismissible is a widget that can be dismissed by swiping left or right. It provides callbacks for onDismissed and confirmDismiss (for showing confirmation dialogs). It supports customizable background widgets shown during the swipe and directional control. It is commonly used in list items for swipe-to-delete or swipe-to-archive functionality."
        },
        {
            "instruction": "What is the Draggable widget in Flutter?",
            "input": "",
            "output": "Draggable is a widget that can be dragged across the screen. It works with DragTarget to create drag-and-drop interfaces. When dragged, it shows a feedback widget that follows the touch point while optionally leaving a childWhenDragging widget in the original position. It carries data of type T that the DragTarget can accept or reject."
        },
        {
            "instruction": "What is the WillPopScope widget in Flutter?",
            "input": "",
            "output": "WillPopScope (replaced by PopScope in newer Flutter versions) intercepts the back button press on Android. Its onWillPop callback returns a Future<bool> — returning true allows navigation back, returning false prevents it. It is used for confirming exit from forms with unsaved changes, implementing double-tap-to-exit, and controlling bottom sheet dismissal."
        },
        {
            "instruction": "What is the RefreshIndicator widget in Flutter?",
            "input": "",
            "output": "RefreshIndicator is a Material Design widget that implements the pull-to-refresh pattern. It wraps a scrollable widget (usually ListView) and shows a circular progress indicator when the user pulls down. Its onRefresh callback returns a Future that resolves when the refresh is complete. It is commonly used for refreshing data from an API."
        },
        {
            "instruction": "What is the Semantics widget in Flutter?",
            "input": "",
            "output": "Semantics is a widget that annotates the widget tree with accessibility information used by screen readers and assistive technologies. It provides labels, hints, values, and actions that describe the widget's purpose and behavior. Many built-in widgets already have semantic annotations, but custom widgets may need explicit Semantics wrapping for accessibility."
        },
        {
            "instruction": "What is the AutomaticKeepAliveClientMixin in Flutter?",
            "input": "",
            "output": "AutomaticKeepAliveClientMixin is a State mixin that prevents a widget from being disposed when it scrolls out of a lazy list (like ListView.builder or PageView). By overriding wantKeepAlive to return true and calling super.build(context), the widget's state is preserved even when off-screen. It is useful for preserving scroll position or form state in tab views."
        },
        {
            "instruction": "What is the difference between Offstage and Visibility in Flutter?",
            "input": "",
            "output": "Both hide widgets, but they differ in behavior. Offstage keeps the widget in the tree and allows it to maintain state, but it still goes through layout — it just doesn't paint or hit-test. Visibility offers more control: it can optionally maintain size (taking up space while invisible), maintain state, animation, and hit testing independently."
        },
        {
            "instruction": "What is the FractionallySizedBox widget in Flutter?",
            "input": "",
            "output": "FractionallySizedBox sizes its child to a fraction of the available space. It takes widthFactor and heightFactor parameters (0.0 to 1.0+) that multiply the parent's dimensions. A widthFactor of 0.5 makes the child half the parent's width. It is useful for responsive layouts where elements should be proportionally sized relative to their container."
        },
        {
            "instruction": "What is the Theme.of(context) method used for in Flutter?",
            "input": "",
            "output": "Theme.of(context) retrieves the nearest ThemeData from the widget tree, giving access to the app's colors, typography, and component themes. It allows widgets to use consistent styling without hardcoded values. For example, Theme.of(context).colorScheme.primary returns the primary color, and Theme.of(context).textTheme.bodyLarge returns the body text style."
        },
        {
            "instruction": "What is the difference between MaterialPageRoute and CupertinoPageRoute?",
            "input": "",
            "output": "MaterialPageRoute uses Android-style transitions: the new page slides up and fades in while the old page slightly slides down and fades. CupertinoPageRoute uses iOS-style transitions: the new page slides in from the right while the old page slides to the left. Both handle back navigation gestures appropriate to their platform."
        },
        {
            "instruction": "What is the showModalBottomSheet function in Flutter?",
            "input": "",
            "output": "showModalBottomSheet displays a Material Design bottom sheet that slides up from the bottom of the screen. It acts as a modal dialog, blocking interaction with the rest of the app. It returns a Future that completes when the sheet is dismissed. It supports customization of shape, background color, constraints, and can be made scrollable for long content."
        },
        {
            "instruction": "What is the PopupMenuButton widget in Flutter?",
            "input": "",
            "output": "PopupMenuButton is a Material Design widget that shows a popup menu when pressed. It takes a list of PopupMenuEntry items (usually PopupMenuItem) and an onSelected callback. The menu appears relative to the button's position. It is commonly used in AppBar actions for 'more options' menus and contextual actions."
        },
        {
            "instruction": "What is the ExpansionTile widget in Flutter?",
            "input": "",
            "output": "ExpansionTile is a ListTile that can expand to reveal hidden children with an animated expand/collapse transition. It displays a header with an optional leading icon and a trailing expand arrow. When tapped, it smoothly reveals its children. It is commonly used in Settings screens, FAQ lists, and nested navigation menus."
        },
        {
            "instruction": "What is the CachedNetworkImage package in Flutter?",
            "input": "",
            "output": "CachedNetworkImage is a Flutter library that loads and caches network images. It downloads images once and stores them locally, showing cached versions on subsequent loads. It provides placeholder and errorWidget builders for loading and error states. It significantly improves performance and user experience by avoiding redundant network requests for images."
        },
        {
            "instruction": "What is the shimmer effect in Flutter?",
            "input": "",
            "output": "The shimmer effect is a loading placeholder animation that displays a gradient wave sweeping across skeleton shapes where content will appear. The shimmer package in Flutter provides this effect. It is used as a better alternative to CircularProgressIndicator for content loading, giving users a preview of the page structure while data is being fetched."
        },
        {
            "instruction": "What is the difference between Opacity and AnimatedOpacity?",
            "input": "",
            "output": "Opacity instantly changes a widget's transparency — there is no transition between states. AnimatedOpacity smoothly animates the opacity change over a specified duration with an optional curve. AnimatedOpacity is an implicit animation widget that automatically handles the animation when the opacity value changes, providing a better user experience for visibility transitions."
        },
        {
            "instruction": "What are extension methods in Dart?",
            "input": "",
            "output": "Extension methods allow adding new functionality to existing classes without modifying their source code or creating subclasses. They are defined using the extension keyword with an on clause specifying the target type. For example, extension StringExtension on String allows adding custom methods to all String objects. They improve code organization and reusability."
        },
        {
            "instruction": "What is a typedef in Dart?",
            "input": "",
            "output": "A typedef creates a named alias for a function type, making function signatures more readable. For example, typedef IntCallback = void Function(int value) defines a type alias for a function that takes an int and returns void. This alias can be used as a parameter type in class definitions and function signatures, improving code clarity."
        },
        {
            "instruction": "What is the factory constructor in Dart?",
            "input": "",
            "output": "A factory constructor in Dart is a constructor that doesn't always create a new instance. It uses the factory keyword and can return cached instances, subtype instances, or instances created through complex logic. Unlike regular constructors, factory constructors can contain return statements. They are commonly used for singleton patterns and fromJson() factories."
        },
        {
            "instruction": "What is the Bloc pattern in Flutter?",
            "input": "",
            "output": "Bloc (Business Logic Component) is a state management pattern that separates business logic from UI using streams. Events are dispatched to a Bloc, which processes them and emits new states. The flutter_bloc package provides BlocProvider for dependency injection, BlocBuilder for rebuilding UI on state changes, and BlocListener for side effects like navigation and snackbars."
        },
        {
            "instruction": "What is the difference between Bloc and Cubit?",
            "input": "",
            "output": "Both are from the bloc package, but they differ in how state changes are triggered. Bloc uses events — you add typed event objects that the Bloc processes through event handlers. Cubit uses methods — you call functions directly that emit new states. Cubit is simpler and requires less boilerplate, making it suitable for straightforward state management. Bloc provides better traceability through the event log."
        },
        {
            "instruction": "What is Riverpod in Flutter?",
            "input": "",
            "output": "Riverpod is a reactive state management and dependency injection framework by the creator of Provider. Unlike Provider, it doesn't depend on BuildContext, supports compile-time safety, and prevents common Provider pitfalls like ProviderNotFoundException. It uses ProviderScope, ref.watch/read for access, and supports auto-disposal, family modifiers, and various provider types."
        },
        {
            "instruction": "What is GetX in Flutter?",
            "input": "",
            "output": "GetX is a lightweight Flutter framework providing state management, dependency injection, and route management. It uses reactive programming with .obs variables and Obx() widgets for minimal boilerplate. GetX also offers Get.to() for navigation, Get.put()/Get.find() for dependency injection, and internationalization support. It prioritizes simplicity but is criticized for tight coupling."
        },
        {
            "instruction": "What is the difference between push, pushReplacement, and pushAndRemoveUntil in Flutter navigation?",
            "input": "",
            "output": "Navigator.push adds a new route on top of the stack (user can go back). pushReplacement replaces the current route with a new one (no back to current). pushAndRemoveUntil pushes a new route and removes all previous routes until a predicate is satisfied — commonly used after login to remove the auth flow from the stack entirely."
        },
        {
            "instruction": "What is the RenderObject in Flutter?",
            "input": "",
            "output": "RenderObject is the low-level class responsible for layout, painting, and hit testing in Flutter. When widgets build, they create Element objects that manage RenderObjects. The RenderObject tree handles the actual visual positioning and drawing. Custom RenderObjects are created by extending RenderBox and implementing performLayout() and paint() for custom layout and rendering behavior."
        },
        {
            "instruction": "What is the Element tree in Flutter?",
            "input": "",
            "output": "The Element tree is an intermediary between the Widget tree and RenderObject tree. When a Widget is instantiated, it creates an Element that holds a reference to both the Widget configuration and the RenderObject. Elements are mutable and persist across rebuilds — they manage updating or replacing their associated Widget and RenderObject during reconciliation."
        },
        {
            "instruction": "What is the difference between the Widget tree, Element tree, and Render tree?",
            "input": "",
            "output": "The Widget tree contains immutable configuration objects that describe the UI. The Element tree contains mutable elements that manage the widget-to-render mapping and lifecycle. The Render tree contains RenderObjects that handle actual layout computation, painting to the screen, and hit testing. Flutter reconciles these three trees during each frame to efficiently update only what changed."
        },
        # ─── Additional Intermediate Questions ─────────────────────────────
        {
            "instruction": "How does Navigator 2.0 differ from Navigator 1.0 in Flutter?",
            "input": "",
            "output": "Navigator 1.0 uses an imperative push/pop API (Navigator.push, Navigator.pop) where the framework manages the route stack. Navigator 2.0 introduces a declarative API with RouterDelegate and RouteInformationParser, giving the developer full control over the page stack. Navigator 2.0 supports deep linking, browser URL syncing, nested navigation, and complex routing logic but requires more boilerplate."
        },
        {
            "instruction": "How does GoRouter simplify navigation in Flutter?",
            "input": "",
            "output": "GoRouter is a declarative routing package built on Navigator 2.0 that simplifies its complexity. It uses a route configuration list with path patterns, supports named routes, path and query parameters, redirect guards, nested navigation with ShellRoute, and deep linking. It automatically syncs with the browser URL on web and provides a simple API: context.go('/path'), context.push('/path')."
        },
        {
            "instruction": "What is the auto_route package in Flutter?",
            "input": "",
            "output": "auto_route is a code-generation routing package that creates type-safe routes from annotated page classes. It generates a router with strongly-typed route classes, eliminating string-based routing errors. It supports nested navigation, route guards, custom transitions, path parameters, and deep linking. Routes are defined using annotations like @RoutePage() and generated with build_runner."
        },
        {
            "instruction": "How does the BLoC pattern implement event-to-state mapping?",
            "input": "",
            "output": "In BLoC, events are dispatched via bloc.add(event) and processed in on<EventType> handlers. Each handler receives the event and an Emitter, and calls emit(newState) to produce states. Handlers can be async, perform API calls, and emit multiple states (loading, success, error). The event-to-state mapping is explicit and testable — each event produces deterministic state transitions."
        },
        {
            "instruction": "What is the Cubit class in the BLoC library?",
            "input": "",
            "output": "Cubit is a simplified version of Bloc that uses direct function calls instead of events. Instead of defining Event classes and event handlers, Cubit exposes methods that directly emit new states. For example, increment() { emit(state + 1); }. Cubit is suitable for simpler state logic while Bloc is preferred for complex event tracking and debugging."
        },
        {
            "instruction": "How does Riverpod improve upon Provider?",
            "input": "",
            "output": "Riverpod is a reactive state management solution that addresses Provider's limitations. It is compile-safe (no runtime ProviderNotFoundException), works without BuildContext, supports auto-disposal, allows multiple providers of the same type, has better testing support, and supports scoping/overriding. Providers are defined globally and accessed via ref.watch/read in ConsumerWidget."
        },
        {
            "instruction": "What are the different types of providers in Riverpod?",
            "input": "",
            "output": "Riverpod provides: Provider (read-only values), StateProvider (simple mutable state), StateNotifierProvider (complex state with StateNotifier), FutureProvider (async data), StreamProvider (stream data), ChangeNotifierProvider (ChangeNotifier-based), and NotifierProvider/AsyncNotifierProvider (Riverpod 2.0 replacements using Notifier class). Each handles different state scenarios."
        },
        {
            "instruction": "How does GetX handle state management in Flutter?",
            "input": "",
            "output": "GetX provides reactive state management with .obs extension and Obx widget. Variables are made observable: var count = 0.obs. Obx(() => Text('$count')) auto-rebuilds on changes. GetX also offers GetBuilder for non-reactive rebuilds, GetxController for business logic, dependency injection via Get.put/Get.lazyPut, route management via Get.to/Get.off, and snackbar/dialog utilities."
        },
        {
            "instruction": "What is the ValueNotifier class in Flutter?",
            "input": "",
            "output": "ValueNotifier is a ChangeNotifier that holds a single value. When the value changes, it notifies its listeners. It is lighter than full state management solutions. Use ValueListenableBuilder to rebuild UI when the value changes. Example: final counter = ValueNotifier<int>(0); counter.value++; triggers rebuilds of ValueListenableBuilder widgets listening to it."
        },
        {
            "instruction": "What is InheritedWidget and how does it work?",
            "input": "",
            "output": "InheritedWidget is the foundational mechanism for passing data down the widget tree efficiently. It sits in the tree and provides data to all descendants. Widgets access it via context.dependOnInheritedWidgetOfExactType<T>(). When data changes, only widgets that registered as dependents are rebuilt. Theme, MediaQuery, and Provider are all built on InheritedWidget."
        },
        {
            "instruction": "How do you implement InheritedNotifier in Flutter?",
            "input": "",
            "output": "InheritedNotifier combines InheritedWidget with a Listenable (ChangeNotifier, ValueNotifier, AnimationController). When the Listenable notifies, the InheritedNotifier automatically triggers dependent widget rebuilds. This eliminates manual setState calls. Create by extending InheritedNotifier<T extends Listenable>, pass the notifier to super, and provide a static of(context) method for access."
        },
        {
            "instruction": "What is the difference between StatelessWidget and StatefulWidget lifecycle?",
            "input": "",
            "output": "StatelessWidget has no mutable state — its build() method is called once on creation and again if the parent rebuilds it with new parameters. StatefulWidget creates a State object with lifecycle: createState → initState → didChangeDependencies → build → didUpdateWidget → setState → deactivate → dispose. State persists across rebuilds until the widget is removed from the tree."
        },
        {
            "instruction": "What is the difference between hot reload and hot restart in Flutter?",
            "input": "",
            "output": "Hot reload injects updated source code into the running Dart VM, preserving app state such as navigation history, form inputs, and variables. It typically takes under a second. Hot restart completely restarts the app, resetting all state back to the initial state while still avoiding a full recompilation. Changes to main() or global initializations require hot restart."
        },
        {
            "instruction": "How do you implement HTTP networking in Flutter?",
            "input": "",
            "output": "Flutter uses the http package for simple HTTP calls: http.get(), http.post(), with responses containing statusCode, body, and headers. For advanced features, the dio package provides interceptors, timeout configuration, request cancellation, FormData upload, download progress, and automatic JSON serialization. Both return Futures that should be awaited, and responses should be decoded from JSON."
        },
        {
            "instruction": "How does the Dio package work in Flutter?",
            "input": "",
            "output": "Dio is a powerful HTTP client for Dart. It supports base URL configuration, interceptors (for auth tokens, logging, error handling), request/response transformation, cancellation via CancelToken, timeout configuration, FormData for file uploads, download with progress callback, and retry logic. Interceptors chain via onRequest, onResponse, and onError callbacks."
        },
        {
            "instruction": "How do you handle JSON serialization in Flutter?",
            "input": "",
            "output": "Flutter handles JSON serialization in two ways: 1) Manual — write fromJson() factory constructor and toJson() method using dart:convert's json.decode/encode. 2) Code generation — use json_serializable and json_annotation packages with build_runner to auto-generate serialization code. The latter reduces boilerplate and errors. Classes annotated with @JsonSerializable() get generated fromJson/toJson."
        },
        {
            "instruction": "What is the json_serializable package in Flutter?",
            "input": "",
            "output": "json_serializable is a code generation package that automatically creates JSON serialization/deserialization code for Dart classes. Classes are annotated with @JsonSerializable() and have a fromJson factory and toJson method that delegate to generated functions. Run 'dart run build_runner build' to generate the .g.dart files. It supports nested objects, enums, custom converters, and field renaming."
        },
        {
            "instruction": "How do you handle form validation in Flutter?",
            "input": "",
            "output": "Flutter forms use Form widget with a GlobalKey<FormState>. Each field uses TextFormField with a validator function that returns null for valid or an error string for invalid input. Call formKey.currentState!.validate() to trigger all validators. autovalidateMode controls when validation runs (onUserInteraction or always). FormState.save() calls each field's onSaved callback."
        },
        {
            "instruction": "How do you implement local storage in Flutter?",
            "input": "",
            "output": "Flutter provides multiple local storage options: SharedPreferences for simple key-value pairs (primitives), sqflite for SQLite databases (structured data), hive for fast NoSQL key-value storage, drift (formerly moor) for type-safe SQLite with reactive queries, and path_provider for getting platform-specific directories to store files. Choice depends on data complexity and performance needs."
        },
        {
            "instruction": "What is the SharedPreferences package in Flutter?",
            "input": "",
            "output": "SharedPreferences provides persistent key-value storage for primitive data types (bool, int, double, String, List<String>). Data is stored in platform-specific locations (NSUserDefaults on iOS, SharedPreferences on Android). It is asynchronous — get instance via SharedPreferences.getInstance(), then use setString(), getBool(), etc. It is ideal for user settings, flags, and small configurations."
        },
        {
            "instruction": "What is the sqflite package in Flutter?",
            "input": "",
            "output": "sqflite provides SQLite database access for Flutter. It supports creating databases, executing raw SQL, batch operations, transactions, and migrations. The openDatabase function creates or opens a database with an onCreate callback for schema creation and onUpgrade for migrations. It is suitable for complex relational data with queries, joins, and indexing needs."
        },
        {
            "instruction": "What is the Hive database package in Flutter?",
            "input": "",
            "output": "Hive is a lightweight, fast key-value NoSQL database for Flutter. It stores data in typed boxes (Box<Type>) with type adapters generated via hive_generator for custom objects. It is faster than sqflite for simple read/write operations, supports encryption, and works on all platforms. Boxes are opened via Hive.openBox() and values accessed via box.get(key), box.put(key, value)."
        },
        {
            "instruction": "How do you implement unit testing in Flutter?",
            "input": "",
            "output": "Unit tests in Flutter use the test package. Tests are written in the test/ directory with _test.dart suffix. Use test() for individual test cases, group() for organizing, setUp/tearDown for test lifecycle. Use expect() with matchers (equals, isNull, throwsException, etc.) for assertions. Run with 'flutter test'. Mock dependencies using mockito or mocktail packages."
        },
        {
            "instruction": "How do you implement widget testing in Flutter?",
            "input": "",
            "output": "Widget tests use flutter_test package with WidgetTester. tester.pumpWidget() renders a widget, tester.tap() simulates taps, tester.enterText() inputs text, tester.pump() triggers rebuilds. find.byType(), find.text(), find.byKey() locate widgets. expect() with matchers like findsOneWidget, findsNothing verify widget state. Widget tests run faster than integration tests without a real device."
        },
        {
            "instruction": "How do you implement integration testing in Flutter?",
            "input": "",
            "output": "Integration tests run the full app on a real device or emulator using the integration_test package. Test files go in integration_test/ directory. They use IntegrationTestWidgetsFlutterBinding.ensureInitialized() and test the complete user flow including navigation, API calls, and persistence. Run with 'flutter test integration_test/'. They are slower but test real app behavior end-to-end."
        },
        {
            "instruction": "What is the mockito package used for in Flutter testing?",
            "input": "",
            "output": "mockito creates mock objects for testing by generating fake implementations of classes. Annotate with @GenerateMocks([ClassName]) and run build_runner to generate mocks. Use when(mock.method()).thenReturn(value) to stub behavior, verify(mock.method()) to check calls, and verifyNever() to ensure methods weren't called. It isolates units from external dependencies like APIs and databases."
        },
        {
            "instruction": "What is the difference between unit tests, widget tests, and integration tests?",
            "input": "",
            "output": "Unit tests verify individual functions, methods, or classes in isolation — fast and focused. Widget tests verify single widgets or small widget groups — render widgets in a test environment without a device. Integration tests verify complete app flows on a real device/emulator — slowest but most realistic. The testing pyramid recommends many unit tests, fewer widget tests, and fewest integration tests."
        },
        {
            "instruction": "How do you implement animations using AnimationController?",
            "input": "",
            "output": "AnimationController drives explicit animations in Flutter. Create it in initState with vsync (from SingleTickerProviderStateMixin), duration, and value range. Use controller.forward(), .reverse(), .repeat() to drive. Add Tween for value mapping and CurvedAnimation for easing. Use AnimatedBuilder or addListener with setState to rebuild. Dispose in dispose() to prevent leaks."
        },
        {
            "instruction": "What is a Tween in Flutter animations?",
            "input": "",
            "output": "Tween defines a mapping between a beginning and ending value for an animation. It interpolates values of any type: Tween<double>(begin: 0, end: 1), ColorTween(begin: red, end: blue), IntTween, etc. Use tween.animate(controller) to create an Animation<T> that maps the controller's 0-1 range to the tween's begin-end range. Chain with CurvedAnimation for easing."
        },
        {
            "instruction": "What are Curves in Flutter animation?",
            "input": "",
            "output": "Curves define the rate of change of an animation over time. Curves.linear is constant speed, Curves.easeIn starts slow, Curves.easeOut ends slow, Curves.bounceOut simulates a bounce, Curves.elasticIn creates a spring effect. Apply via CurvedAnimation(parent: controller, curve: Curves.easeInOut). Custom curves can be created by extending the Curve class."
        },
        {
            "instruction": "How do you implement staggered animations in Flutter?",
            "input": "",
            "output": "Staggered animations use a single AnimationController with multiple Tweens that animate at different intervals. Each animation uses an Interval curve: CurvedAnimation(parent: controller, curve: Interval(0.0, 0.5)) animates during the first half. By overlapping or sequencing intervals, multiple properties animate in a choreographed sequence — like opacity fading in while position slides up."
        },
        {
            "instruction": "What is the TweenAnimationBuilder widget in Flutter?",
            "input": "",
            "output": "TweenAnimationBuilder is an implicit animation widget that animates between any two values using a Tween. Unlike AnimatedContainer which only handles specific properties, TweenAnimationBuilder works with any Tween type. It takes a tween, duration, builder, and optional onEnd callback. It handles creating and managing the AnimationController internally."
        },
        {
            "instruction": "How do you implement page route transitions in Flutter?",
            "input": "",
            "output": "Custom page transitions use PageRouteBuilder with transitionsBuilder that receives animation and secondaryAnimation. Return transition widgets like FadeTransition, SlideTransition, ScaleTransition, or RotationTransition. For named routes, override onGenerateRoute and return custom PageRoute subclasses. The transitionDuration and reverseTransitionDuration control timing."
        },
        {
            "instruction": "How do you implement responsive design in Flutter?",
            "input": "",
            "output": "Responsive Flutter design uses: MediaQuery for screen size/orientation, LayoutBuilder for parent constraints, Flexible/Expanded for proportional sizing, Wrap for flow layouts, and breakpoint-based layouts that switch between mobile/tablet/desktop views. The flutter_screenutil package helps with dimension adaptation. Grid systems and adaptive widgets adjust columns and spacing based on screen width."
        },
        {
            "instruction": "What is the adaptive vs responsive design approach in Flutter?",
            "input": "",
            "output": "Responsive design adjusts the same layout to fit different screen sizes (e.g., changing column count in a grid). Adaptive design creates entirely different layouts for different platforms or form factors (e.g., BottomNavigationBar on mobile, NavigationRail on tablet, Drawer on desktop). Flutter supports both through LayoutBuilder, Platform checks, and adaptive widget constructors."
        },
        {
            "instruction": "How do you implement theming in Flutter?",
            "input": "",
            "output": "Theming uses ThemeData configured in MaterialApp's theme property. ThemeData defines colorScheme, textTheme, elevatedButtonTheme, inputDecorationTheme, and 30+ component themes. Dark mode is supported via darkTheme property. Access theme data with Theme.of(context). Material 3 uses ColorScheme.fromSeed() for harmonious colors. ThemeExtension enables custom theme properties."
        },
        {
            "instruction": "How do you implement dark mode in Flutter?",
            "input": "",
            "output": "Dark mode is implemented by providing both theme (light) and darkTheme (dark) ThemeData in MaterialApp. themeMode controls which is active: ThemeMode.system (follow device setting), ThemeMode.light, or ThemeMode.dark. MediaQuery.platformBrightnessOf(context) detects the current brightness. All colors should use theme-aware references like Theme.of(context).colorScheme.surface."
        },
        {
            "instruction": "How does the Stream class work in Dart?",
            "input": "",
            "output": "Stream delivers a sequence of asynchronous events over time. Single-subscription streams allow one listener (like file reading), while broadcast streams allow multiple listeners (like user events). Listen with stream.listen(), transform with map/where/expand, combine with merge/zip. Use StreamController to create streams, async* with yield to generate them, and StreamBuilder to display them in UI."
        },
        {
            "instruction": "What is a StreamController in Dart?",
            "input": "",
            "output": "StreamController creates and controls a Stream. It provides a sink for adding events (controller.add(), controller.addError(), controller.close()) and a stream for listening. StreamController() creates single-subscription, StreamController.broadcast() creates broadcast streams. Always close controllers in dispose() to prevent memory leaks. The stream can be accessed via controller.stream."
        },
        {
            "instruction": "What is the StreamBuilder widget in Flutter?",
            "input": "",
            "output": "StreamBuilder rebuilds its UI whenever a Stream emits a new event. It provides an AsyncSnapshot containing connectionState (none, waiting, active, done), data, and error. The builder handles each state: waiting → show loading, active with data → show content, active with error → show error, done → show final state. It automatically subscribes and unsubscribes from the stream."
        },
        {
            "instruction": "What is the FutureBuilder widget in Flutter?",
            "input": "",
            "output": "FutureBuilder rebuilds its UI based on the state of a Future. It provides an AsyncSnapshot with connectionState and data/error. Common pattern: waiting → show CircularProgressIndicator, done with data → show content, done with error → show error message. Important: don't create the Future inside build() — store it in a variable to prevent infinite rebuilds."
        },
        {
            "instruction": "How do you implement push notifications in Flutter?",
            "input": "",
            "output": "Push notifications use the firebase_messaging package with Firebase Cloud Messaging (FCM). Setup involves adding Firebase to the project, requesting permission on iOS, getting the device token for targeting, and handling messages in three states: foreground (onMessage stream), background (onBackgroundMessage handler), and terminated (getInitialMessage). flutter_local_notifications shows notification UI."
        },
        {
            "instruction": "How do you implement local notifications in Flutter?",
            "input": "",
            "output": "Local notifications use the flutter_local_notifications package. Initialize with platform-specific settings (AndroidInitializationSettings, DarwinInitializationSettings). Show notifications with show() method, schedule with zonedSchedule(), and handle taps via onDidReceiveNotificationResponse callback. Notifications are customized with channels (Android), sound, vibration, icons, and action buttons."
        },
        {
            "instruction": "How do you implement Firebase Authentication in Flutter?",
            "input": "",
            "output": "Firebase Auth uses the firebase_auth package. Initialize Firebase in main(). Sign in methods: signInWithEmailAndPassword, createUserWithEmailAndPassword, signInWithCredential (Google/Apple), signInAnonymously. Listen to auth state via authStateChanges() stream. FirebaseAuth.instance.currentUser provides the current user. Implement sign out with signOut(). Handle errors with FirebaseAuthException."
        },
        {
            "instruction": "How do you implement Cloud Firestore in Flutter?",
            "input": "",
            "output": "Cloud Firestore uses the cloud_firestore package for real-time NoSQL database access. Collections hold documents with fields. CRUD operations: add() creates documents, get() reads, update() modifies, delete() removes. Real-time updates via snapshots() stream. Queries support where(), orderBy(), limit(), startAfter() for pagination. Transactions ensure atomic operations."
        },
        {
            "instruction": "How do you implement image picking in Flutter?",
            "input": "",
            "output": "Image picking uses the image_picker package. ImagePicker().pickImage(source: ImageSource.gallery) or ImageSource.camera returns an XFile. Configure maxWidth, maxHeight, and imageQuality. On iOS, add camera and photo library usage descriptions to Info.plist. On Android, camera permission is needed in AndroidManifest.xml. Display picked images with Image.file(File(xFile.path))."
        },
        {
            "instruction": "How do you implement file downloading in Flutter?",
            "input": "",
            "output": "File downloading uses the dio package for progress tracking: dio.download(url, savePath, onReceiveProgress: callback). Use path_provider to get the download directory. For background downloads, use flutter_downloader package. Handle permissions with permission_handler. Show progress with StreamBuilder or ValueListenableBuilder connected to the download progress callback."
        },
        {
            "instruction": "How do you implement deep linking in Flutter?",
            "input": "",
            "output": "Deep linking opens specific app screens from URLs. On Android, configure intent filters in AndroidManifest.xml. On iOS, set up Associated Domains and Universal Links. In Flutter, use GoRouter or Navigator 2.0 to handle incoming URLs. uni_links or app_links package provides a stream of incoming links. Verify links with assetlinks.json (Android) and apple-app-site-association (iOS)."
        },
        {
            "instruction": "What is the Connectivity Plus package in Flutter?",
            "input": "",
            "output": "connectivity_plus checks and monitors network connectivity status. Connectivity().checkConnectivity() returns the current connection type (wifi, mobile, none). Connectivity().onConnectivityChanged provides a Stream of connection changes. It detects connection type but not actual internet availability — use an HTTP ping to verify actual connectivity."
        },
        {
            "instruction": "How do you implement internationalization (i18n) in Flutter?",
            "input": "",
            "output": "Flutter i18n uses the flutter_localizations package and intl package. Define localization delegates in MaterialApp (GlobalMaterialLocalizations, GlobalWidgetsLocalizations, GlobalCupertinoLocalizations). Create ARB files for translations and generate Dart code with gen_l10n. Access translations via AppLocalizations.of(context)!.helloWorld. The locale is set via MaterialApp's locale property."
        },
        {
            "instruction": "What is the intl package used for in Flutter?",
            "input": "",
            "output": "The intl package provides internationalization utilities: DateFormat for locale-aware date formatting, NumberFormat for number and currency formatting, Intl.message for translatable strings, Bidi for bidirectional text support, and plural/gender handling. It is the foundation for Flutter's localization system and works with ARB files and code generation."
        },
        {
            "instruction": "How do you manage environment variables in Flutter?",
            "input": "",
            "output": "Environment variables in Flutter are managed using: 1) --dart-define flag: flutter run --dart-define=API_KEY=value, accessed via String.fromEnvironment('API_KEY'). 2) .env files with flutter_dotenv package. 3) Compile-time configuration files per environment. Never hardcode secrets — use --dart-define for build-time injection and exclude .env files from version control."
        },
        {
            "instruction": "What is the difference between MaterialApp and CupertinoApp?",
            "input": "",
            "output": "MaterialApp uses Material Design widgets (Scaffold, AppBar, FloatingActionButton) following Google's design language. CupertinoApp uses Cupertino widgets (CupertinoPageScaffold, CupertinoNavigationBar) following Apple's iOS design language. Both provide theming, routing, and localization. MaterialApp.router and CupertinoApp.router support Navigator 2.0. Choose based on target platform design requirements."
        },
        {
            "instruction": "What is the difference between MaterialPageRoute and CupertinoPageRoute?",
            "input": "",
            "output": "MaterialPageRoute uses a bottom-to-top slide transition (Android-style) when navigating to a new page. CupertinoPageRoute uses a right-to-left slide transition with parallax (iOS-style). Both support fullscreenDialog for bottom-to-top modal presentation. Use PageRouteBuilder for custom transitions. The routes also differ in back-swipe gesture behavior."
        },
        {
            "instruction": "How do you implement caching strategies in Flutter?",
            "input": "",
            "output": "Flutter caching strategies include: in-memory cache with Map or LRU (cache_manager package), HTTP response caching with dio_cache_interceptor, image caching (built into Image.network via ImageCache), SQLite for persistent cache, Hive for key-value cache, and flutter_cache_manager for file caching. Cache invalidation uses TTL, max-age headers, or manual clearing."
        },
        {
            "instruction": "What is the difference between mainAxisAlignment and crossAxisAlignment?",
            "input": "",
            "output": "In Row, mainAxisAlignment controls horizontal alignment (start, end, center, spaceBetween, spaceAround, spaceEvenly) and crossAxisAlignment controls vertical alignment (start, end, center, stretch, baseline). In Column, they swap — mainAxisAlignment is vertical and crossAxisAlignment is horizontal. Main axis follows the direction of the Flex layout."
        },
        {
            "instruction": "How do you implement pagination in Flutter?",
            "input": "",
            "output": "Pagination is implemented using ScrollController to detect when the user reaches the bottom: controller.position.pixels >= controller.position.maxScrollExtent. Then load the next page of data. Common patterns: offset-based (page number), cursor-based (last item ID), and infinite scroll with loading indicators. Packages like infinite_scroll_pagination handle this pattern with caching and error states."
        },
        {
            "instruction": "How do you implement pull-to-refresh with pagination?",
            "input": "",
            "output": "Combine RefreshIndicator with ScrollController-based pagination. RefreshIndicator's onRefresh resets the page counter and reloads the first page. ScrollController's listener detects scroll-to-bottom for loading the next page. Maintain loading state to prevent duplicate requests. Show a loading indicator at the bottom of the list while fetching the next page."
        },
        {
            "instruction": "What is the Freezed package in Flutter?",
            "input": "",
            "output": "Freezed is a code generation package for creating immutable data classes with value equality. Annotate classes with @freezed and define factory constructors. Generated code includes copyWith() for immutable updates, toString(), == operator, hashCode, JSON serialization (with json_serializable), and union types for sealed classes. It eliminates boilerplate for data models."
        },
        {
            "instruction": "What is the Equatable package in Flutter?",
            "input": "",
            "output": "Equatable simplifies value equality by auto-generating == and hashCode based on specified properties. Extend Equatable and override get props to return a list of properties to compare: List<Object?> get props => [name, age]. This eliminates manual == and hashCode boilerplate and is commonly used with BLoC state classes to ensure proper equality checks."
        },
        {
            "instruction": "How do you implement error handling in Flutter apps?",
            "input": "",
            "output": "Flutter error handling includes: try-catch for expected errors, FlutterError.onError for framework errors (caught in Widget build), PlatformDispatcher.instance.onError for uncaught async errors, runZonedGuarded for zone-level error capture. Display errors with ErrorWidget.builder for custom error screens. Use Result/Either patterns for functional error propagation."
        },
        {
            "instruction": "What is the Either type pattern in Flutter?",
            "input": "",
            "output": "Either (from dartz or fpdart package) represents a value that is one of two types: Left (typically failure) or Right (typically success). Instead of throwing exceptions, functions return Either<Failure, Success>. Callers handle both cases with fold((failure) => ..., (success) => ...). This makes error handling explicit, composable, and forces callers to handle errors."
        },
        {
            "instruction": "How do you implement dependency injection in Flutter?",
            "input": "",
            "output": "Dependency injection in Flutter uses: get_it (service locator with singleton/factory registration), injectable (code-gen for get_it), Provider/Riverpod (DI via widget tree), or manual constructor injection. get_it registers dependencies at startup: getIt.registerSingleton<ApiService>(ApiServiceImpl()). Tests override with mock implementations. DI decouples components for testability."
        },
        {
            "instruction": "What is the get_it package in Flutter?",
            "input": "",
            "output": "get_it is a service locator for dependency injection. Register types at startup with registerSingleton (single instance), registerFactory (new instance each call), or registerLazySingleton (created on first access). Retrieve with GetIt.instance<Type>() or getIt<Type>(). It supports named registrations, async initialization, and test overrides with allowReassignment."
        },
        {
            "instruction": "How do you implement the Repository pattern in Flutter?",
            "input": "",
            "output": "The Repository pattern abstracts data sources behind a common interface. Define an abstract class with methods like getUsers(), and implement it with concrete classes (RemoteRepository using API, LocalRepository using database). The domain layer depends on the abstract repository, not implementations. Use DI to inject the correct implementation. This enables easy testing and data source swapping."
        },
        {
            "instruction": "What is Clean Architecture in Flutter?",
            "input": "",
            "output": "Clean Architecture divides the app into layers: Presentation (UI, BLoC/Cubit, Pages), Domain (Entities, Use Cases, Repository interfaces), and Data (Repository implementations, Data Sources, Models). Dependencies point inward — Data depends on Domain, Presentation depends on Domain. Domain has no Flutter dependencies. This ensures testability, maintainability, and independence from frameworks."
        },
        {
            "instruction": "What is the MVVM pattern in Flutter?",
            "input": "",
            "output": "MVVM (Model-View-ViewModel) separates: Model (data and business logic), View (UI widgets that display state), ViewModel (holds UI state and exposes methods for the View). In Flutter, ViewModel can be a ChangeNotifier, StateNotifier, or Cubit. The View observes the ViewModel via Provider/Riverpod/BlocBuilder. Commands from the View call ViewModel methods that update state."
        },
        {
            "instruction": "How do you implement the Singleton pattern in Dart?",
            "input": "",
            "output": "Singleton in Dart uses a factory constructor with a static instance: class Database { static final Database _instance = Database._internal(); factory Database() => _instance; Database._internal(); }. This ensures only one instance exists. Access via Database(). Alternatively, use a static field: static final instance = Database._internal(). Top-level variables in Dart are also lazy singletons."
        },
        {
            "instruction": "How do you handle keyboard visibility in Flutter?",
            "input": "",
            "output": "Keyboard visibility is detected via MediaQuery.of(context).viewInsets.bottom — a non-zero value means the keyboard is visible. The flutter_keyboard_visibility package provides a stream of keyboard visibility changes. To dismiss the keyboard, call FocusScope.of(context).unfocus() or FocusManager.instance.primaryFocus?.unfocus(). Wrap scrollable content to prevent keyboard overlap."
        },
        {
            "instruction": "How do you implement a splash screen in Flutter?",
            "input": "",
            "output": "Native splash screens use the flutter_native_splash package which generates platform-specific splash screens from pubspec.yaml configuration. This appears before Flutter engine loads. For an animated splash after engine startup, create a splash screen widget with animations that navigates to the home screen after completion. Both approaches can be combined for seamless transition."
        },
        {
            "instruction": "How do you generate app icons in Flutter?",
            "input": "",
            "output": "The flutter_launcher_icons package generates platform-specific app icons from a single source image. Configure in pubspec.yaml with image path, background color, and platform-specific options (adaptive icons on Android, rounded corners on iOS). Run 'dart run flutter_launcher_icons' to generate all required icon sizes. The source image should be at least 1024x1024 pixels."
        },
        {
            "instruction": "What is the path_provider package in Flutter?",
            "input": "",
            "output": "path_provider provides access to platform-specific file system directories. getApplicationDocumentsDirectory() returns the persistent app documents directory. getTemporaryDirectory() returns a temp directory that may be cleared. getApplicationSupportDirectory() returns platform support directory. getExternalStorageDirectory() returns Android external storage. These paths are needed for file I/O operations."
        },
        {
            "instruction": "How do you implement biometric authentication in Flutter?",
            "input": "",
            "output": "Biometric authentication uses the local_auth package. Check availability with canCheckBiometrics and getAvailableBiometrics(). Authenticate with authenticate(localizedReason: 'Please authenticate') which returns a bool. Configure Android with USE_BIOMETRIC permission and iOS with Face ID usage description. Support includes fingerprint, face recognition, and iris scanning."
        },
        {
            "instruction": "What is the permission_handler package in Flutter?",
            "input": "",
            "output": "permission_handler manages runtime permissions across platforms. Request with Permission.camera.request(), check with Permission.camera.status. Status values: granted, denied, permanentlyDenied, restricted. For permanently denied, guide users to app settings via openAppSettings(). Configure required permissions in AndroidManifest.xml and Info.plist. Group related permissions for better UX."
        },
        {
            "instruction": "How do you implement platform-specific code in Flutter?",
            "input": "",
            "output": "Platform-specific code uses MethodChannel for communicating between Dart and native code. Define a channel: const channel = MethodChannel('com.app/channel'). Invoke methods: await channel.invokeMethod('getName'). Implement handlers in Kotlin/Java (Android) and Swift/Objective-C (iOS). For simple platform checks, use Platform.isAndroid, Platform.isIOS from dart:io, or Theme.of(context).platform."
        },
        {
            "instruction": "What is the MethodChannel in Flutter?",
            "input": "",
            "output": "MethodChannel enables bidirectional method calls between Dart and native platform code. Dart calls native: await channel.invokeMethod('method', args). Native calls Dart: channel.setMethodCallHandler(handler). Arguments are auto-serialized using StandardMessageCodec. Supported types include null, bool, int, double, String, List, Map, and Uint8List. It is used for accessing platform-specific APIs."
        },
        {
            "instruction": "What is the EventChannel in Flutter?",
            "input": "",
            "output": "EventChannel enables streaming data from native platform code to Dart. The native side sets up a StreamHandler with onListen and onCancel callbacks. Dart receives a Stream via eventChannel.receiveBroadcastStream(). It is used for continuous data like sensor readings, location updates, Bluetooth data, and battery state changes that naturally produce a stream of events."
        },
        {
            "instruction": "How do you implement WebSocket communication in Flutter?",
            "input": "",
            "output": "WebSocket communication uses web_socket_channel package. Create connection: WebSocketChannel.connect(Uri.parse('ws://server')). Send data: channel.sink.add(message). Receive data: channel.stream.listen((data) {}). Close: channel.sink.close(). Use StreamBuilder to display incoming messages in UI. Handle reconnection logic for dropped connections. The socket_io_client package provides Socket.IO support."
        },
        {
            "instruction": "How do you implement a bottom navigation bar with persistent pages?",
            "input": "",
            "output": "Use IndexedStack with BottomNavigationBar to persist page state. IndexedStack keeps all pages alive but only shows the selected one: IndexedStack(index: currentIndex, children: pages). This preserves scroll position and form state across tab switches. For memory efficiency, use AutomaticKeepAliveClientMixin on pages that need persistence without keeping all pages alive."
        },
        {
            "instruction": "What is the AutomaticKeepAliveClientMixin in Flutter?",
            "input": "",
            "output": "AutomaticKeepAliveClientMixin keeps a State alive in a lazy-loaded scrollable (TabBarView, PageView, ListView) even when scrolled off-screen. Mix it into State, override wantKeepAlive to return true, and call super.build(context) in build. Without it, tabs in TabBarView rebuild when switching — with it, state and scroll position are preserved."
        },
        {
            "instruction": "How do you implement CustomPainter in Flutter?",
            "input": "",
            "output": "CustomPainter draws custom graphics on a Canvas. Extend CustomPainter, override paint(Canvas canvas, Size size) to draw shapes, paths, text, and images. Override shouldRepaint() to control when to redraw. Wrap in CustomPaint widget to display. Canvas methods include drawRect, drawCircle, drawPath, drawLine, drawArc, and drawImage. Use for charts, custom decorations, and games."
        },
        {
            "instruction": "What are the common Canvas drawing methods in Flutter?",
            "input": "",
            "output": "Canvas provides: drawRect/drawRRect (rectangles), drawCircle/drawOval (circles/ovals), drawLine (lines), drawPath (custom paths), drawArc (arcs), drawPoints (point sets), drawImage/drawImageRect (images), drawParagraph (text). Each takes a Paint object for styling (color, strokeWidth, style, shader). Combine with Path for complex shapes using moveTo, lineTo, quadraticBezierTo, cubicTo."
        },
        {
            "instruction": "How do you implement a custom clipper in Flutter?",
            "input": "",
            "output": "Custom clippers extend CustomClipper<Path> and override getClip(Size size) to return a Path defining the clip shape. Use with ClipPath(clipper: MyClipper()). The path can create any shape — waves, curves, polygons. Override shouldReclip() to control when the clip is recalculated. Custom clippers are used for shaped containers, custom app bars, and decorative edges."
        },
        {
            "instruction": "How do you implement drag and drop in Flutter?",
            "input": "",
            "output": "Flutter provides Draggable<T> for draggable items and DragTarget<T> for drop zones. Draggable has child (default appearance), feedback (while dragging), childWhenDragging (placeholder), and onDragCompleted. DragTarget has builder (showing drop state) and onAcceptWithDetails callback. LongPressDraggable requires a long press to start dragging. Data of type T is passed from Draggable to DragTarget."
        },
        {
            "instruction": "How do you implement a Dismissible list in Flutter?",
            "input": "",
            "output": "Dismissible wraps a list item to enable swipe-to-dismiss. It takes a key (unique per item), direction, onDismissed callback, and optional background/secondaryBackground for left/right swipe visuals. The confirmDismiss callback returns a Future<bool> for confirmation dialogs. Used in ListView.builder for swipe-to-delete or swipe-to-archive patterns."
        },
        {
            "instruction": "What is the ReorderableListView widget in Flutter?",
            "input": "",
            "output": "ReorderableListView displays a list whose items can be reordered by long-pressing and dragging. Each child needs a unique key. The onReorder callback receives old and new indices to update the data. ReorderableListView.builder provides lazy building for long lists. It is used for sortable lists like playlists, task priorities, and settings ordering."
        },
        {
            "instruction": "How do you implement the BLoC testing pattern?",
            "input": "",
            "output": "BLoC testing uses the bloc_test package. blocTest<Bloc, State>() creates a test with build (create bloc), act (add events), expect (assert states), verify (check side effects). Test initial state, event processing, error handling, and state transitions. Mock dependencies with mockito. Example: blocTest('emits [Loading, Loaded]', build: () => MyBloc(), act: (b) => b.add(LoadEvent()), expect: () => [Loading(), Loaded(data)])."
        },
        {
            "instruction": "How does the Isolate.run function work in Dart?",
            "input": "",
            "output": "Isolate.run (Dart 2.19+) is a simplified API for running computations in a separate isolate. It takes a function and returns a Future with the result: final result = await Isolate.run(() => expensiveComputation()). The function runs in a new isolate, preventing UI jank. It handles isolate creation, message passing, and cleanup automatically. The function's return value must be sendable."
        },
        {
            "instruction": "How do you implement a search feature with debouncing in Flutter?",
            "input": "",
            "output": "Debounced search uses a Timer that resets on each keystroke. In the TextField's onChanged, cancel the previous timer and start a new one: timer?.cancel(); timer = Timer(Duration(milliseconds: 500), () => performSearch(query)). This delays the search until the user stops typing for 500ms, reducing API calls. With RxDart, use debounceTime on the stream."
        },
        {
            "instruction": "What is the url_launcher package in Flutter?",
            "input": "",
            "output": "url_launcher opens URLs in the default browser, phone dialer, email client, or SMS app. Use launchUrl(Uri.parse(url)) with mode parameter: platformDefault, inAppWebView, or externalApplication. Check availability with canLaunchUrl(). Supported schemes: https://, tel:, mailto:, sms:. Configure allowed schemes in AndroidManifest.xml queries and Info.plist LSApplicationQueriesSchemes."
        },
        {
            "instruction": "How do you implement secure storage in Flutter?",
            "input": "",
            "output": "flutter_secure_storage stores data in the platform's secure keystore — Keychain on iOS and EncryptedSharedPreferences or KeyStore on Android. Use for tokens, passwords, and sensitive data. API is simple: write(key: 'token', value: 'abc'), read(key: 'token'), delete(key: 'token'). Data survives app reinstall on iOS (optional) and is encrypted at rest."
        },
        {
            "instruction": "What is the Bloc Observer in the BLoC library?",
            "input": "",
            "output": "BlocObserver monitors all Bloc/Cubit instances globally. Override onCreate, onEvent, onChange, onTransition, onError, and onClose to log state changes, track analytics, or report errors. Set via Bloc.observer = MyObserver(). It provides a centralized location for debugging and monitoring all state management activity across the entire application."
        },
        {
            "instruction": "How do you handle different screen sizes with breakpoints in Flutter?",
            "input": "",
            "output": "Define breakpoints like: compact (<600dp), medium (600-840dp), expanded (>840dp). Use LayoutBuilder or MediaQuery to read screen width. Switch layouts at breakpoints: if (width < 600) MobileLayout() else if (width < 840) TabletLayout() else DesktopLayout(). Packages like responsive_framework provide breakpoint templates. Test all breakpoints with DevicePreview."
        },
        {
            "instruction": "How do you implement custom transitions with PageRouteBuilder?",
            "input": "",
            "output": "PageRouteBuilder creates routes with custom transitions. It takes pageBuilder (the destination page) and transitionsBuilder (the animation). transitionsBuilder receives context, animation, secondaryAnimation, and child. Combine animation with SlideTransition, FadeTransition, ScaleTransition, or RotationTransition. Chain CurvedAnimation for easing effects. Set transitionDuration for timing control."
        },
        {
            "instruction": "What is the Shimmer effect and how to implement it in Flutter?",
            "input": "",
            "output": "Shimmer effect is a loading placeholder animation that shows a glistening sweep across content shapes. Implement using the shimmer package: Shimmer.fromColors(baseColor: grey[300], highlightColor: grey[100], child: placeholderWidget). Create placeholder widgets matching the expected content layout (circles for avatars, rectangles for text lines) to provide visual feedback during data loading."
        },
        {
            "instruction": "How do you implement a carousel/slider in Flutter?",
            "input": "",
            "output": "Carousels use PageView with PageController(viewportFraction: 0.8) for visible adjacent pages. The carousel_slider package provides auto-play, infinite scroll, custom layout, and indicators. For smooth snapping, use PageView.custom with physics. Add page indicators using smooth_page_indicator or dots_indicator packages. Control programmatically via PageController.animateToPage()."
        },
        {
            "instruction": "What is the difference between shrinkWrap and physics in ListView?",
            "input": "",
            "output": "shrinkWrap: true makes ListView size itself to its content instead of expanding to fill available space. This is needed when ListView is inside Column but is expensive for long lists (measures all items). physics controls scroll behavior: NeverScrollableScrollPhysics disables scrolling, BouncingScrollPhysics adds iOS bounce, ClampingScrollPhysics adds Android clamp. Use shrinkWrap sparingly."
        },
        {
            "instruction": "How do you implement text editing with TextEditingController?",
            "input": "",
            "output": "TextEditingController manages the text content and selection of a TextField. Create in initState(), dispose in dispose(). Access text via controller.text, set text programmatically, listen to changes with addListener(). Provide to TextField via controller property. Use controller.selection to get/set cursor position and selection range. Clear with controller.clear()."
        },
        {
            "instruction": "What are Widget keys used for in Flutter?",
            "input": "",
            "output": "Keys help Flutter's reconciliation algorithm identify and preserve widget state. ValueKey uses a value for identity, ObjectKey uses object identity, UniqueKey is always unique, GlobalKey provides access to state from anywhere. Keys are essential in lists (ListView.builder items), animated lists, Form fields, and when reordering widgets to preserve state correctly."
        },
        {
            "instruction": "How do you implement a CustomScrollView in Flutter?",
            "input": "",
            "output": "CustomScrollView composes scrollable layouts using slivers. It takes a list of slivers: SliverAppBar (collapsible header), SliverList (list), SliverGrid (grid), SliverToBoxAdapter (any widget), SliverPadding (spacing), SliverPersistentHeader (sticky headers), SliverFillRemaining (footer). All slivers share one scroll position for a unified scroll experience."
        },
        {
            "instruction": "What is SliverAppBar and how does it work?",
            "input": "",
            "output": "SliverAppBar is a Material Design app bar that integrates with CustomScrollView for scroll-based effects. Key properties: floating (reappears on scroll up), pinned (remains at minimum height), snap (snaps to full/collapsed), expandedHeight (expanded size), flexibleSpace (expandable content with FlexibleSpaceBar). It collapses, stretches, and fades content based on scroll position."
        },
        {
            "instruction": "How do you implement state restoration in Flutter?",
            "input": "",
            "output": "State restoration preserves UI state (scroll position, form input, navigation stack) when the OS kills the app. Use RestorationMixin in State, register RestorableProperties (RestorableInt, RestorableString, RestorableTextEditingController). Set restorationId on MaterialApp and navigators. The system serializes state to disk and restores it when the app is recreated."
        },
        {
            "instruction": "What is the difference between spread operator and addAll in Dart?",
            "input": "",
            "output": "The spread operator (...) inlines collection elements into another collection: [1, 2, ...list3]. addAll() adds elements to an existing list: list.addAll(otherList). Spread is used in collection literals and is preferred in Flutter's build methods for composing widget lists. The null-aware spread (...?) safely handles null collections. addAll mutates the list in place."
        },
        {
            "instruction": "How do you implement the Observer pattern in Flutter?",
            "input": "",
            "output": "The Observer pattern in Flutter uses ChangeNotifier with notifyListeners(), ValueNotifier with value changes, Streams with StreamController, or the BLoC pattern with event/state streams. Widgets observe via ListenableBuilder, ValueListenableBuilder, StreamBuilder, or BlocBuilder. NavigatorObserver, RouteObserver, and WidgetsBindingObserver observe framework events."
        },
        {
            "instruction": "How do you implement GraphQL in Flutter?",
            "input": "",
            "output": "GraphQL in Flutter uses the graphql_flutter package. Wrap the app with GraphQLProvider and configure GraphQLClient with cache and link (HttpLink for API endpoint). Use Query widget for data fetching and Mutation widget for modifications. Define queries as strings with gql(). The package handles caching, pagination, subscriptions, and optimistic UI updates."
        },
        {
            "instruction": "How do you implement WebView in Flutter?",
            "input": "",
            "output": "WebView in Flutter uses the webview_flutter package. WebViewController configures the WebView: loadRequest (URL), navigationDelegate (intercept navigation), JavaScriptMode.unrestricted (enable JS), addJavaScriptChannel (Dart-JS communication). The WebViewWidget displays the content. On Android, requires internet permission. On iOS, requires App Transport Security configuration for HTTP URLs."
        },
        {
            "instruction": "How do you implement maps in Flutter?",
            "input": "",
            "output": "Google Maps uses the google_maps_flutter package. Configure API keys for Android (AndroidManifest.xml) and iOS (AppDelegate). GoogleMap widget takes initialCameraPosition, markers, polylines, polygons, and onMapCreated callback for GoogleMapController. For OpenStreetMap, use flutter_map package with TileLayer. Both support markers, camera animation, and user location."
        },
        {
            "instruction": "How do you implement location services in Flutter?",
            "input": "",
            "output": "Location services use the geolocator package. Request permission with Geolocator.requestPermission(). Get current position with getCurrentPosition(desiredAccuracy: LocationAccuracy.high). Track position with getPositionStream(). geocoding package converts coordinates to addresses (reverse geocoding) and addresses to coordinates (geocoding). Handle permission denied and service disabled states."
        },
        {
            "instruction": "What is the flutter_bloc vs BLoC pattern difference?",
            "input": "",
            "output": "BLoC pattern is an architectural pattern using Streams for state management — events in, states out. flutter_bloc is a library implementing this pattern with Bloc/Cubit classes, BlocProvider for DI, BlocBuilder for UI rebuilds, BlocListener for side effects, and BlocConsumer for both. flutter_bloc adds convenience over raw StreamController-based BLoC implementation."
        },
        {
            "instruction": "How do you implement the SOLID principles in Flutter?",
            "input": "",
            "output": "SOLID in Flutter: Single Responsibility — each widget/class has one purpose. Open/Closed — extend via composition not modification. Liskov Substitution — subclasses should be interchangeable. Interface Segregation — small, focused abstract classes. Dependency Inversion — depend on abstractions (repository interfaces), not implementations. These principles guide clean, maintainable Flutter architecture."
        },
        {
            "instruction": "How do you implement offline-first architecture in Flutter?",
            "input": "",
            "output": "Offline-first stores data locally first, then syncs with the server. Use Hive/sqflite for local data, connectivity_plus to detect network status, and a sync queue for pending operations. On connectivity restored, replay queued operations. Conflict resolution strategies include last-write-wins, server-wins, and manual merge. Cache API responses for offline reading."
        },
        {
            "instruction": "How do you implement video playback in Flutter?",
            "input": "",
            "output": "Video playback uses the video_player package. Initialize VideoPlayerController with network URL, asset, or file. Call controller.initialize() (async), then play(), pause(), seekTo(). Display with AspectRatio and VideoPlayer widget. Overlay custom controls. The chewie package provides pre-built controls with fullscreen, playback speed, and progress bar."
        },
        {
            "instruction": "How do you implement audio playback in Flutter?",
            "input": "",
            "output": "Audio playback uses just_audio or audioplayers packages. just_audio supports network, asset, and file playback with features like looping, speed control, volume, seeking, buffering state, and playlist support. Initialize AudioPlayer, setUrl/setAsset, then play(). Listen to playerStateStream, positionStream, and durationStream for UI updates. Handle audio focus and background playback."
        },
        {
            "instruction": "What is the Dart analyzer and how to configure it?",
            "input": "",
            "output": "The Dart analyzer performs static analysis on Dart code, checking for type errors, unused variables, deprecated APIs, and code style. It is configured via analysis_options.yaml in the project root. Rules are defined under linter: rules: section. Include rule sets like flutter_lints or very_good_analysis. Custom rules can be enabled/disabled. Severity can be set to error, warning, or info."
        },
        {
            "instruction": "How do you implement code generation with build_runner in Flutter?",
            "input": "",
            "output": "build_runner automates code generation from annotations. Packages like json_serializable, freezed, auto_route, and mockito use it. Add build_runner and generators as dev_dependencies. Run 'dart run build_runner build' for one-time generation or 'dart run build_runner watch' for continuous regeneration. Generated files have .g.dart or .freezed.dart extensions. Add part directives in source files."
        },
        {
            "instruction": "How do you implement flavor/variant builds in Flutter?",
            "input": "",
            "output": "Flavors create different app variants (dev, staging, prod) with different configurations. Android uses productFlavors in build.gradle with different applicationId, app name, and icons per flavor. iOS uses Xcode schemes and configurations. Flutter connects via --flavor flag and --dart-define for environment variables. The flutter_flavorizr package automates the setup process."
        },
        {
            "instruction": "What is the AnimatedList widget in Flutter?",
            "input": "",
            "output": "AnimatedList is a scrollable list that animates items when they are inserted or removed. Use a GlobalKey<AnimatedListState> to call insertItem(index) and removeItem(index, builder). The builder provides an Animation<double> for transition effects during insertion and removal. It provides smooth visual feedback for dynamic list changes like adding or deleting items."
        },
        {
            "instruction": "How do you implement custom scroll physics in Flutter?",
            "input": "",
            "output": "Custom scroll physics extend ScrollPhysics and override methods like applyPhysicsToUserOffset, applyBoundaryConditions, and createBallisticSimulation. Common customizations: snapping to items (PageScrollPhysics), custom friction, bounce resistance, and overscroll behavior. Use with ScrollView's physics property. Chain physics with parent parameter for composition: MyPhysics(parent: BouncingScrollPhysics())."
        },
        {
            "instruction": "How do you implement app state persistence in Flutter?",
            "input": "",
            "output": "App state persistence saves state across app restarts. Options: SharedPreferences for simple values, Hive for structured data, SQLite for relational data, or JSON files for serializable objects. Save state on changes using debouncing. Hydrated BLoC automatically persists and restores BLoC state using JSON serialization. Load persisted state during app initialization."
        },
        {
            "instruction": "What is the difference between SingleChildScrollView and ListView?",
            "input": "",
            "output": "SingleChildScrollView wraps a single child widget (like Column) and makes it scrollable when it overflows. It renders all content at once — suitable for short content. ListView builds items lazily (with .builder), rendering only visible items — suitable for long lists. Use SingleChildScrollView for forms and short pages, ListView.builder for long dynamic lists."
        },
        {
            "instruction": "How do you implement gradient buttons in Flutter?",
            "input": "",
            "output": "Gradient buttons wrap a button with a DecoratedBox or Container with gradient decoration: Container(decoration: BoxDecoration(gradient: LinearGradient(colors: [color1, color2])), child: ElevatedButton(style: ElevatedButton.styleFrom(backgroundColor: Colors.transparent, shadowColor: Colors.transparent), ...)). Or use Ink widget with Ink(decoration: gradient, child: InkWell)."
        },
        {
            "instruction": "How do you implement multi-language support in Flutter?",
            "input": "",
            "output": "Multi-language support uses Flutter's localization system. Define supported locales in MaterialApp's supportedLocales. Create ARB files for each language (app_en.arb, app_es.arb). Configure l10n.yaml for code generation. Access strings via AppLocalizations.of(context)!.greeting. Handle text direction (LTR/RTL) with Directionality widget. Use intl package for plurals, dates, and number formatting."
        },
        {
            "instruction": "How do you implement a chat UI in Flutter?",
            "input": "",
            "output": "Chat UI uses a reversed ListView.builder for messages with ScrollController for auto-scroll. Each message is a Row with Align/Container for left (received) or right (sent) alignment. A TextField with send button at the bottom for input. Use StreamBuilder for real-time message updates. WebSocket or Firebase Firestore provides real-time data. Add timestamps, read receipts, and typing indicators."
        },
        # ─── More Intermediate Questions (Batch 3) ─────────────────────────────
        {
            "instruction": "How do you implement multi-provider setup in Flutter?",
            "input": "",
            "output": "MultiProvider wraps multiple providers efficiently: MultiProvider(providers: [ChangeNotifierProvider(create: (_) => AuthProvider()), Provider(create: (_) => ApiService()), StreamProvider(create: (_) => locationStream)], child: MyApp()). This is cleaner than nesting providers manually. Providers are created in order, so later providers can depend on earlier ones using ProxyProvider."
        },
        {
            "instruction": "What is ProxyProvider in the Provider package?",
            "input": "",
            "output": "ProxyProvider creates a provider that depends on other providers' values. ProxyProvider<A, B> takes provider A's value to create provider B: ProxyProvider<AuthService, ApiService>(update: (_, auth, __) => ApiService(auth.token)). It updates B when A changes. ProxyProvider2, ProxyProvider3, etc. support multiple dependencies. ChangeNotifierProxyProvider works with ChangeNotifiers."
        },
        {
            "instruction": "How do you implement a custom theme in Flutter?",
            "input": "",
            "output": "Custom themes define ThemeData with ColorScheme, TextTheme, and component themes. Use ColorScheme.fromSeed(seedColor: Colors.blue) for Material 3. Override component themes: elevatedButtonTheme, inputDecorationTheme, cardTheme, etc. Create custom theme extensions with ThemeExtension for app-specific tokens. Apply in MaterialApp's theme. Access with Theme.of(context)."
        },
        {
            "instruction": "How do you implement a loading overlay in Flutter?",
            "input": "",
            "output": "Loading overlay uses Stack with a conditional overlay: Stack(children: [mainContent, if (isLoading) Container(color: Colors.black54, child: Center(child: CircularProgressIndicator()))]). Or use the loading_overlay package. Block taps during loading with AbsorbPointer. Show fullscreen loading with showDialog and CircularProgressIndicator. Use ModalBarrier for semi-transparent blocking."
        },
        {
            "instruction": "How do you implement app routing with named routes?",
            "input": "",
            "output": "Named routes are defined in MaterialApp's routes map: routes: {'/': (_) => HomeScreen(), '/profile': (_) => ProfileScreen()}. Navigate with Navigator.pushNamed(context, '/profile'). For dynamic routes with arguments, use onGenerateRoute with RouteSettings. Pass arguments via Navigator.pushNamed(context, '/detail', arguments: id). Retrieve with ModalRoute.of(context)!.settings.arguments."
        },
        {
            "instruction": "How do you implement bottom sheet with scrollable content?",
            "input": "",
            "output": "Scrollable bottom sheet uses showModalBottomSheet with isScrollControlled: true and DraggableScrollableSheet inside. The DraggableScrollableSheet provides initialChildSize, minChildSize, maxChildSize for drag behavior. Inside, use ListView.builder or CustomScrollView. Set the outer Container's height with MediaQuery for proper sizing. Add a drag handle indicator at the top."
        },
        {
            "instruction": "How do you implement a search bar in Flutter?",
            "input": "",
            "output": "Flutter provides SearchBar widget (Material 3) and SearchAnchor for an integrated search experience. The traditional approach uses AppBar with a TextField replacing the title on search mode toggle. SearchDelegate with showSearch() provides a full-screen search experience. For filtering lists, use a TextField with onChanged that filters a list and updates state."
        },
        {
            "instruction": "How do you handle back button press in Flutter?",
            "input": "",
            "output": "Handle back button with PopScope (Flutter 3.12+): PopScope(canPop: false, onPopInvokedWithResult: (didPop, result) { if (!didPop) showExitDialog(context); }, child: scaffold). This replaces the deprecated WillPopScope. For custom back behavior in navigation, use Navigator.maybePop() which respects route predicates. On Android, the system back gesture triggers pop."
        },
        {
            "instruction": "How do you implement screen transitions in Flutter?",
            "input": "",
            "output": "Screen transitions are customized via PageRouteBuilder with transitionsBuilder. Common transitions: SlideTransition (slide from side), FadeTransition (fade in), ScaleTransition (zoom), RotationTransition (rotate). Combine multiple transitions with AnimatedBuilder. The animations package provides SharedAxisTransition, FadeThroughTransition, and FadeScaleTransition for Material motion patterns."
        },
        {
            "instruction": "How do you implement infinite scrolling in Flutter?",
            "input": "",
            "output": "Infinite scrolling uses ScrollController with listener in ListView.builder. When position.pixels >= position.maxScrollExtent - threshold, trigger loading next page. Track currentPage, isLoading, and hasMore states. Show a loading indicator as the last item. Cancel loading on dispose. Package infinite_scroll_pagination handles pagination state, error recovery, and first/last page indicators."
        },
        {
            "instruction": "How do you implement state management with ChangeNotifier?",
            "input": "",
            "output": "ChangeNotifier is a simple observable class. Extend it to create a model: class Counter extends ChangeNotifier { int _count = 0; int get count => _count; void increment() { _count++; notifyListeners(); } }. Provide with ChangeNotifierProvider. Consume with Consumer<Counter> or context.watch<Counter>(). Call notifyListeners() after state changes to trigger UI rebuilds."
        },
        {
            "instruction": "How do you implement a timer in Flutter?",
            "input": "",
            "output": "Timer class from dart:async provides two types: Timer(Duration(seconds: 5), callback) for one-shot delayed execution, Timer.periodic(Duration(seconds: 1), callback) for repeated execution. Cancel with timer.cancel(). For UI-driven timers, use AnimationController or Stream.periodic. Always cancel timers in dispose() to prevent memory leaks and callbacks on disposed widgets."
        },
        {
            "instruction": "How do you implement shared element transitions between screens?",
            "input": "",
            "output": "Shared element transitions use the Hero widget. Wrap a widget on the source screen with Hero(tag: 'unique-tag', child: Image()). Wrap the corresponding widget on the destination screen with the same Hero tag. When navigating, Flutter automatically animates the widget flying between the two positions. The tag must be unique within each screen's Hero scope."
        },
        {
            "instruction": "How do you implement a stepper form wizard in Flutter?",
            "input": "",
            "output": "Stepper widget creates a step-by-step form wizard. Define each Step with title, content (form fields), and state (indexed, editing, complete). Track currentStep index. Handle onStepContinue (validate and advance), onStepCancel (go back), and onStepTapped (jump to step). Validate each step's form before advancing. Use StepperType.horizontal for horizontal layout."
        },
        {
            "instruction": "How do you implement custom dialog in Flutter?",
            "input": "",
            "output": "Custom dialogs use showDialog with a Dialog widget or custom Container. Control size with ConstrainedBox, shape with RoundedRectangleBorder. Dismiss with Navigator.pop(context, result). Return values via the showDialog Future. Use showGeneralDialog for full customization including transition animation, barrier color, and barrier label. Add form fields, images, or any widget inside."
        },
        {
            "instruction": "How do you implement a rating widget in Flutter?",
            "input": "",
            "output": "Rating widgets use a Row of IconButtons with star icons. Track selected rating in state. Change icon between Icons.star (filled) and Icons.star_border (empty) based on index vs rating. Add half-star support with Icons.star_half. Use GestureDetector for drag-based rating. Packages like flutter_rating_bar provide ready-made interactive rating bars with customizable shapes."
        },
        {
            "instruction": "How do you implement SharedPreferences with change listeners?",
            "input": "",
            "output": "SharedPreferences doesn't have built-in change listeners. Wrap it with a ChangeNotifier or ValueNotifier: class PrefsNotifier extends ChangeNotifier { Future<void> setTheme(bool dark) async { await prefs.setBool('dark', dark); notifyListeners(); } }. Provide with ChangeNotifierProvider. Alternatively, use streaming_shared_preferences package for reactive SharedPreferences."
        },
        {
            "instruction": "How do you implement gesture-based animations in Flutter?",
            "input": "",
            "output": "Gesture-based animations combine GestureDetector with AnimationController. On drag/pan updates, update the controller's value based on gesture delta. On drag end, use controller.forward() or controller.reverse() based on velocity to complete the animation. SpringSimulation adds physics-based completion. This pattern is used for swipe-to-dismiss, pull-to-refresh, and draggable sheets."
        },
        {
            "instruction": "How do you implement Platform-adaptive widgets in Flutter?",
            "input": "",
            "output": "Platform-adaptive widgets check the platform and render accordingly. Use Theme.of(context).platform or Platform.isIOS. Create adaptive widgets: Widget adaptiveButton() => Platform.isIOS ? CupertinoButton(...) : ElevatedButton(...). Flutter provides .adaptive constructors: Switch.adaptive, Slider.adaptive, CircularProgressIndicator.adaptive that automatically use platform-appropriate styling."
        },
        {
            "instruction": "How do you implement text overflow handling in Flutter?",
            "input": "",
            "output": "Text overflow is handled with the overflow property: TextOverflow.ellipsis (shows ...), clip (clips text), fade (fades out), visible (overflows visibly). Combine with maxLines to limit lines: Text('Long text', maxLines: 2, overflow: TextOverflow.ellipsis). For dynamic text sizing, use FittedBox or auto_size_text package which adjusts font size to fit available space."
        },
        {
            "instruction": "How do you implement Firebase Cloud Storage in Flutter?",
            "input": "",
            "output": "Firebase Cloud Storage uses the firebase_storage package. Upload files with: ref.putFile(file) or ref.putData(bytes) with optional SettableMetadata. Track progress with uploadTask.snapshotEvents stream. Get download URL with ref.getDownloadURL(). List files with ref.listAll(). Delete with ref.delete(). Set security rules for authentication-based access control."
        },
        {
            "instruction": "How do you implement custom scroll effects in Flutter?",
            "input": "",
            "output": "Custom scroll effects use NotificationListener<ScrollNotification> to react to scroll position. Read metrics.pixels, maxScrollExtent, and velocity. Apply effects with AnimatedBuilder or ValueNotifier. For parallax, offset image based on scroll position. For app bar color change, interpolate color based on scroll progress. For sticky headers, use SliverPersistentHeader with custom delegate."
        },
        {
            "instruction": "How do you implement a countdown timer widget in Flutter?",
            "input": "",
            "output": "Countdown timers use Timer.periodic with Duration(seconds: 1) that decrements remaining time each tick. Store remaining seconds in state, display formatted time. Cancel timer when reaching zero or in dispose(). For more precise timing, use Stopwatch or DateTime.difference. Update UI with setState or StreamBuilder with Stream.periodic. Use AnimationController for animated countdown arcs."
        },
        {
            "instruction": "What is the difference between Navigator.pop and Navigator.maybePop?",
            "input": "",
            "output": "Navigator.pop immediately pops the current route without checking PopScope/WillPopScope. Navigator.maybePop first checks if popping is allowed — it respects PopScope's canPop value and calls onPopInvoked. If the route says it can't be popped, maybePop does nothing. Always prefer maybePop when triggered programmatically to respect route guards. The system back button uses maybePop."
        },
        {
            "instruction": "How do you implement a collapsible sidebar in Flutter?",
            "input": "",
            "output": "Collapsible sidebar uses AnimatedContainer or AnimatedAlign within a Row. Toggle width between expanded (250) and collapsed (70) states. Show icons only when collapsed, icons + labels when expanded. Use LayoutBuilder to determine if sidebar should auto-collapse based on screen width. NavigationRail with extended property provides this pattern with Material Design styling."
        },
        {
            "instruction": "How do you implement QR code scanning in Flutter?",
            "input": "",
            "output": "QR code scanning uses the mobile_scanner or qr_code_scanner packages. mobile_scanner provides MobileScanner widget with onDetect callback returning BarcodeCapture. Configure camera facing, torch, zoom, and barcode formats. For QR code generation, use the qr_flutter package with QrImageView widget. Handle camera permissions with permission_handler. Test on physical devices."
        },
        {
            "instruction": "How do you implement copy to clipboard in Flutter?",
            "input": "",
            "output": "Clipboard operations use the Clipboard class from services.dart. Copy: await Clipboard.setData(ClipboardData(text: 'Hello')). Paste: final data = await Clipboard.getData(Clipboard.kTextPlain); String? text = data?.text. Show confirmation with SnackBar after copying. On web, clipboard access may require user gesture and browser permission."
        },
        {
            "instruction": "How do you implement skeleton loading screens in Flutter?",
            "input": "",
            "output": "Skeleton loading creates placeholder widgets matching expected content layout. Use Container with decoration showing content shapes (rectangles for text, circles for avatars). Apply shimmer effect with the shimmer package. Create a skeleton version of your screen that matches the real layout dimensions. Toggle between skeleton and real content based on loading state."
        },
        {
            "instruction": "How do you manage multiple TextEditingControllers in a form?",
            "input": "",
            "output": "Create controllers in initState: nameCtrl = TextEditingController(); emailCtrl = TextEditingController(). Dispose all in dispose to prevent memory leaks. For dynamic forms, use a Map<String, TextEditingController> or List. Set initial values: controller = TextEditingController(text: initialValue). Access values: nameCtrl.text. Listen to changes: controller.addListener(callback)."
        },
        {
            "instruction": "How do you implement a custom app bar in Flutter?",
            "input": "",
            "output": "Custom app bars use PreferredSize widget wrapping a Container or custom widget. Set preferredSize: PreferredSize(preferredSize: Size.fromHeight(80), child: MyCustomAppBar()). Or use flexibleSpace in AppBar for custom expansion. For gradient app bars, use Container with BoxDecoration(gradient). In CustomScrollView, use SliverPersistentHeader with a custom delegate."
        },
        {
            "instruction": "How do you implement state management using setState?",
            "input": "",
            "output": "setState is the simplest state management for StatefulWidget. Call setState(() { _counter++; }) to update state and trigger a rebuild. setState must not be async — perform async work first, then call setState with results. Only use setState for widget-local state. For shared state across widgets, use Provider, BLoC, or Riverpod. setState causes a full rebuild of the widget's subtree."
        },
        {
            "instruction": "How do you implement a custom paint chart in Flutter?",
            "input": "",
            "output": "Custom charts use CustomPainter. For bar charts: draw rectangles with drawRect at calculated positions. For line charts: use drawPath connecting data points with lineTo. For pie charts: use drawArc for each segment. Add labels with TextPainter. Animate with AnimationController driving CustomPainter via repaint notifier. Packages fl_chart and syncfusion_flutter_charts provide ready-made chart widgets."
        },
        {
            "instruction": "How do you implement the MVC pattern in Flutter?",
            "input": "",
            "output": "MVC in Flutter: Model holds data and business logic, View is the widget tree (build method), Controller mediates between Model and View (handles user input, updates model, triggers view updates). The Controller can be a separate class injected via Provider or GetX. While Flutter naturally supports MVVM better, MVP and MVC patterns work with proper separation."
        },
        # ─── More Intermediate Questions (Batch 4) ─────────────────────────────
        {
            "instruction": "How do you implement a splash screen in Flutter?",
            "input": "",
            "output": "Native splash screens use the flutter_native_splash package. Configure in pubspec.yaml: flutter_native_splash with color, image, android_12 settings. Run dart run flutter_native_splash:create. For in-app splash: display a splash widget first, perform initialization in initState or FutureBuilder, then navigate to home screen. Remove native splash with FlutterNativeSplash.remove() after init completes."
        },
        {
            "instruction": "How do you implement retry logic for network requests in Flutter?",
            "input": "",
            "output": "Retry logic wraps HTTP calls with exponential backoff. Implement with a retry loop: for (int i = 0; i < maxRetries; i++) { try { return await dio.get(url); } catch (e) { if (i == maxRetries - 1) rethrow; await Future.delayed(Duration(seconds: pow(2, i))); } }. Dio interceptors provide built-in retry. The retry package offers configurable retry strategies."
        },
        {
            "instruction": "How do you implement pull-to-refresh in Flutter?",
            "input": "",
            "output": "Pull-to-refresh uses RefreshIndicator wrapping a scrollable widget: RefreshIndicator(onRefresh: () async { await fetchData(); }, child: ListView(...)). The onRefresh callback must return a Future. For Cupertino style, use CupertinoSliverRefreshControl inside CustomScrollView. Customize the indicator's color, displacement, and strokeWidth. The gesture triggers when pulling down at the top of the list."
        },
        {
            "instruction": "How do you implement offline-first architecture in Flutter?",
            "input": "",
            "output": "Offline-first stores data locally first, then syncs with the server. Use sqflite or Hive for local storage. Check connectivity with connectivity_plus. Queue write operations when offline with an operation queue. Sync pending operations when online. Use ETags or last-modified timestamps for efficient sync. Implement conflict resolution (server wins, client wins, or merge). Cache API responses with timestamps."
        },
        {
            "instruction": "How do you implement a file download with progress in Flutter?",
            "input": "",
            "output": "Dio supports download progress: await dio.download(url, savePath, onReceiveProgress: (received, total) { setState(() => progress = received / total); }). Display progress with LinearProgressIndicator(value: progress). For background downloads, use flutter_downloader. Request storage permission with permission_handler. Get save path with path_provider's getApplicationDocumentsDirectory()."
        },
        {
            "instruction": "How do you implement biometric authentication in Flutter?",
            "input": "",
            "output": "Biometric auth uses local_auth package. Check availability: canCheckBiometrics, getAvailableBiometrics(). Authenticate: await auth.authenticate(localizedReason: 'Verify identity', options: AuthenticationOptions(biometricOnly: true)). Handle success/failure. Requires AndroidManifest.xml permission USE_BIOMETRIC and iOS Info.plist NSFaceIDUsageDescription. Test on physical devices."
        },
        {
            "instruction": "How do you implement a date picker in Flutter?",
            "input": "",
            "output": "showDatePicker presents a material date picker: final date = await showDatePicker(context: context, initialDate: DateTime.now(), firstDate: DateTime(2000), lastDate: DateTime(2100)). For time: showTimePicker. For date range: showDateRangePicker. Cupertino style uses CupertinoDatePicker in a bottom sheet. Format dates with intl package's DateFormat: DateFormat('yyyy-MM-dd').format(date)."
        },
        {
            "instruction": "How do you implement a multi-select list in Flutter?",
            "input": "",
            "output": "Multi-select uses a Set<T> to track selected items. ListView.builder with CheckboxListTile: CheckboxListTile(value: selectedSet.contains(item), onChanged: (v) { setState(() => v! ? selectedSet.add(item) : selectedSet.remove(item)); }). Show selection count. Add select all / deselect all buttons. Use FilterChip for tag-based multi-select."
        },
        {
            "instruction": "How do you implement image cropping in Flutter?",
            "input": "",
            "output": "Image cropping uses the image_cropper package. After picking an image with image_picker, pass it to ImageCropper: final croppedFile = await ImageCropper().cropImage(sourcePath: pickedFile.path, aspectRatioPresets: [CropAspectRatioPreset.square], uiSettings: [AndroidUiSettings(toolbarTitle: 'Crop')]). Returns the cropped file path or null if cancelled."
        },
        {
            "instruction": "How do you implement analytics tracking in Flutter?",
            "input": "",
            "output": "Firebase Analytics: add firebase_analytics package. Log events: FirebaseAnalytics.instance.logEvent(name: 'purchase', parameters: {'item': 'widget'}). Track screens: FirebaseAnalyticsObserver as navigatorObserver. Set user properties: setUserProperty(name: 'role', value: 'admin'). Alternative SDKs: Amplitude, Mixpanel, PostHog. Create an AnalyticsService abstraction for easy switching between providers."
        },
        {
            "instruction": "How do you implement drag and drop in Flutter?",
            "input": "",
            "output": "Drag and drop uses Draggable and DragTarget widgets. Draggable wraps a widget to make it draggable — define child, feedback (shown while dragging), and childWhenDragging. DragTarget defines onWillAcceptWithDetails (validation), onAcceptWithDetails (handle drop), and builder (visual response). LongPressDraggable requires long press to start. ReorderableListView provides built-in reorderable list."
        },
        {
            "instruction": "How do you implement a custom TabBar indicator?",
            "input": "",
            "output": "Custom TabBar indicators extend Decoration. Override createBoxPainter to return a custom BoxPainter that draws the indicator: class CircleIndicator extends Decoration { @override BoxPainter createBoxPainter([VoidCallback? onChanged]) => _CirclePainter(); }. In _CirclePainter, override paint to draw circles, lines, or any shape at the tab position. Apply via TabBar's indicator property."
        },
        {
            "instruction": "How do you implement social login in Flutter?",
            "input": "",
            "output": "Google Sign-In: google_sign_in package, call GoogleSignIn().signIn() then authenticate with Firebase. Apple Sign-In: sign_in_with_apple package with ASAuthorizationAppleIDButton. Facebook: flutter_facebook_auth. GitHub: use OAuth2 web flow with url_launcher. Link accounts in Firebase Auth with linkWithCredential. Store tokens securely. Handle sign-out from all providers."
        },
        {
            "instruction": "How do you implement a responsive grid layout?",
            "input": "",
            "output": "Responsive grids adapt columns to screen width. Use LayoutBuilder to get constraints, calculate crossAxisCount: (constraints.maxWidth / 200).floor(). GridView.builder with SliverGridDelegateWithFixedCrossAxisCount or WithMaxCrossAxisExtent. Alternatively, use Wrap with fixed-width children for flowing layout. The responsive_grid or flutter_staggered_grid_view packages add more responsive grid options."
        },
        {
            "instruction": "How do you implement custom validators in Flutter forms?",
            "input": "",
            "output": "Custom validators are functions returning String? (null = valid): String? validateEmail(String? value) { if (value == null || !RegExp(r'^[a-zA-Z0-9.]+@[a-zA-Z0-9]+\\.[a-zA-Z]+').hasMatch(value)) return 'Invalid email'; return null; }. Assign to TextFormField's validator property. Combine multiple validators: [required, minLength(3), matchesPattern(regex)]. Validate on submit with formKey.currentState!.validate()."
        },
        {
            "instruction": "How do you implement encrypted storage in Flutter?",
            "input": "",
            "output": "flutter_secure_storage uses platform keystore (Keychain on iOS, EncryptedSharedPreferences on Android). Write: await storage.write(key: 'token', value: 'abc'). Read: await storage.read(key: 'token'). Delete: await storage.delete(key: 'token'). Configure Android with AndroidOptions(encryptedSharedPreferences: true). For file encryption, use encrypt package with AES-256. Never hardcode encryption keys."
        },
        {
            "instruction": "How do you implement custom error handling in Flutter?",
            "input": "",
            "output": "FlutterError.onError handles framework errors: FlutterError.onError = (details) { logger.log(details.exception); }. PlatformDispatcher.instance.onError catches unhandled async errors. Zone.current.handleUncaughtError catches zone errors. Use runZonedGuarded for app-wide error catching. Create custom exception classes extending Exception. Use Result/Either types for typed error handling."
        },
        {
            "instruction": "How do you implement app versioning and updates in Flutter?",
            "input": "",
            "output": "App version comes from pubspec.yaml version field (e.g., 1.2.3+4). Access at runtime with package_info_plus: PackageInfo.fromPlatform(). Force update checks: compare installed version with server's minimum version. Show update dialog if outdated. Use in_app_update (Android) for seamless updates. Use upgrader package for cross-platform update prompts with store links."
        },
        {
            "instruction": "How do you implement a floating action button menu in Flutter?",
            "input": "",
            "output": "FAB menu uses FloatingActionButton with AnimationController to expand/collapse mini FABs. On press, animate mini FABs sliding up with SlideTransition. Use Transform.translate or Positioned in a Stack. Toggle rotation animation on the main FAB icon. SpeedDial from flutter_speed_dial provides a ready-made solution with labels and icons for each action."
        },
        {
            "instruction": "How do you implement data caching with expiry in Flutter?",
            "input": "",
            "output": "Data caching with expiry stores timestamps alongside data. Check if cache is stale: if (DateTime.now().difference(cachedTime) > Duration(hours: 1)) { fetchFresh(); }. Implement with Hive: store CacheEntry(data, timestamp). SharedPreferences works for simple key-value caches. HTTP caching respects Cache-Control headers. Dio's dio_cache_interceptor handles HTTP caching automatically."
        },
        {
            "instruction": "How do you implement a signature pad in Flutter?",
            "input": "",
            "output": "Signature pads use CustomPainter with GestureDetector. Track touch points in onPanUpdate, add to a Path. In CustomPainter's paint, draw the path with a Paint configured for stroke width, color, and StrokeCap.round. Clear by resetting the path. Export as image with PictureRecorder. The signature package provides a ready-made Signature widget with undo, redo, and export functionality."
        },
        {
            "instruction": "How do you implement real-time data with Firestore?",
            "input": "",
            "output": "Firestore real-time data uses snapshots() which returns a Stream. Listen with StreamBuilder: StreamBuilder<QuerySnapshot>(stream: FirebaseFirestore.instance.collection('messages').orderBy('time').snapshots(), builder: (ctx, snap) { ... }). The stream emits on any document change (added, modified, removed). Check docChanges for granular change types. Unsubscribe on dispose."
        },
        {
            "instruction": "How do you implement responsive text sizing in Flutter?",
            "input": "",
            "output": "Responsive text uses MediaQuery to scale: double scaleFactor = MediaQuery.of(context).size.width / 375; Text('Hello', style: TextStyle(fontSize: 16 * scaleFactor)). Or use textScaleFactor from MediaQuery. FittedBox auto-sizes text to fit container. auto_size_text package auto-adjusts font size. For accessibility, respect user's textScaleFactor settings rather than overriding them."
        },
        {
            "instruction": "How do you implement a photo gallery in Flutter?",
            "input": "",
            "output": "Photo gallery uses GridView.builder displaying thumbnails. Tap to open full-screen with Hero animation and PageView for swiping. Use photo_view package for pinch-to-zoom. Load images lazily with CachedNetworkImage. Show image count and current index. Add share and download actions. For device photos, use photo_manager to access the device gallery. Implement multi-select for batch operations."
        },
        {
            "instruction": "How do you implement an onboarding flow in Flutter?",
            "input": "",
            "output": "Onboarding uses PageView with PageController for swipeable intro screens. Display dots indicator with PageIndicator or custom Row of AnimatedContainers. Each page shows an image, title, and description. Add Skip and Next buttons. On last page, show Get Started button. Store completion in SharedPreferences. Check on app start to skip if already completed. Use smooth_page_indicator for animated dots."
        },
        {
            "instruction": "How do you implement app localization with ARB files?",
            "input": "",
            "output": "Flutter localization uses .arb files in lib/l10n/. Enable in pubspec.yaml: flutter: generate: true. Create app_en.arb with JSON key-value pairs and placeholders. Run flutter gen-l10n to generate AppLocalizations class. Access: AppLocalizations.of(context)!.helloWorld. Add more locales with app_es.arb, app_fr.arb. Support plurals with ICU message syntax. Configure supportedLocales and localizationsDelegates in MaterialApp."
        },
        {
            "instruction": "How do you implement a carousel slider in Flutter?",
            "input": "",
            "output": "Carousel sliders use PageView with PageController(viewportFraction: 0.8) for partial next/prev page visibility. Add auto-scroll with Timer.periodic calling controller.nextPage(). Show dots indicator. Apply transforms in itemBuilder for scale/opacity effects. The carousel_slider package provides a ready-made CarouselSlider with autoPlay, enlargeCenterPage, and custom layout options."
        },
        {
            "instruction": "How do you implement a settings screen in Flutter?",
            "input": "",
            "output": "Settings screens use ListView with ListTile, SwitchListTile, and sections. Group settings with padding/dividers. SwitchListTile for boolean settings. ListTile with trailing text/icons for navigation to sub-settings. Store preferences with SharedPreferences or Hive. Use SettingsList from the settings_ui package for platform-adaptive settings UI. Notify the app of changes via Provider or callbacks."
        },
        {
            "instruction": "How do you implement connectivity monitoring in Flutter?",
            "input": "",
            "output": "connectivity_plus monitors network status. Check current: ConnectivityResult result = await Connectivity().checkConnectivity(). Listen to changes: Connectivity().onConnectivityChanged.listen((result) { ... }). Result types: wifi, mobile, ethernet, none. Note: connectivity_plus checks network interface, not actual internet access. For internet validation, try pinging a server with InternetConnectionChecker."
        },
        {
            "instruction": "How do you implement a barcode scanner in Flutter?",
            "input": "",
            "output": "Barcode scanning uses mobile_scanner package. MobileScannerController manages camera. MobileScanner widget with onDetect returns BarcodeCapture containing list of Barcodes with rawValue, format, and type. Supports 1D (EAN, UPC, Code128) and 2D (QR, DataMatrix) formats. Configure torch, facing camera, and detection speed. Handle permissions gracefully. Test on physical devices only."
        },
        {
            "instruction": "How do you implement Riverpod's AsyncNotifier?",
            "input": "",
            "output": "AsyncNotifier handles async state with built-in loading/error handling. Create: class UsersNotifier extends AsyncNotifier<List<User>> { @override Future<List<User>> build() async => await api.getUsers(); Future<void> addUser(User u) async { state = const AsyncLoading(); state = await AsyncValue.guard(() => api.addUser(u)); } }. final usersProvider = AsyncNotifierProvider<UsersNotifier, List<User>>(UsersNotifier.new). Consume with ref.watch and .when(data:, loading:, error:)."
        },
        {
            "instruction": "How do you implement BLoC-to-BLoC communication?",
            "input": "",
            "output": "BLoC-to-BLoC communication options: 1) Inject one BLoC into another via constructor for direct access. 2) Use StreamSubscription to listen to another BLoC's stream. 3) In the UI layer, use BlocListener on one BLoC to add events to another. 4) Use a shared repository/service both BLoCs depend on. 5) Event bus pattern with a shared Stream. Option 3 is recommended for clarity."
        },
        {
            "instruction": "How do you implement reusable widgets in Flutter?",
            "input": "",
            "output": "Reusable widgets accept configuration via constructor parameters. Accept required and optional parameters with defaults. Use callbacks for events: onTap, onChanged. Accept Widget? parameters for customizable slots. Use generic types for type-safe data widgets. Extract common patterns into widget classes. Keep widget responsibility single. Document public API with doc comments. Test with widget tests."
        },
        {
            "instruction": "How do you implement file upload with multipart in Flutter?",
            "input": "",
            "output": "Multipart file upload with Dio: FormData formData = FormData.fromMap({'file': await MultipartFile.fromFile(path, filename: 'photo.jpg'), 'name': 'test'}). Send: await dio.post('/upload', data: formData, onSendProgress: (sent, total) { progress = sent/total; }). With http package: var request = http.MultipartRequest('POST', url)..files.add(await http.MultipartFile.fromPath('file', path))."
        },
        {
            "instruction": "How do you implement PDF viewing in Flutter?",
            "input": "",
            "output": "PDF viewing uses syncfusion_flutter_pdfviewer or pdfx packages. SfPdfViewer.network(url) or SfPdfViewer.asset('assets/doc.pdf') renders PDFs with zoom, scroll, and page navigation. For PDF generation, use pdf package: final doc = pw.Document(); doc.addPage(pw.Page(build: (context) => pw.Text('Hello'))); final bytes = await doc.save(). Save or share the generated PDF."
        },
        {
            "instruction": "How do you implement FCM push notifications setup?",
            "input": "",
            "output": "Firebase Cloud Messaging setup: add firebase_messaging and firebase_core packages. Initialize Firebase. Request permission: await FirebaseMessaging.instance.requestPermission(). Get token: await FirebaseMessaging.instance.getToken(). Handle foreground: FirebaseMessaging.onMessage.listen((msg) { showNotification(msg); }). Handle background: FirebaseMessaging.onBackgroundMessage(handler). Handle notification tap: FirebaseMessaging.onMessageOpenedApp.listen(...)."
        },
        {
            "instruction": "How do you implement custom MapMarkers in Flutter?",
            "input": "",
            "output": "Custom map markers with google_maps_flutter: convert Widget to BitmapDescriptor using WidgetToImage approach — use RepaintBoundary with GlobalKey, capture with toImage(), convert to bytes. Create Marker(markerId: id, position: latLng, icon: customIcon). For simpler custom icons, use BitmapDescriptor.fromAssetImage(config, 'assets/pin.png'). Update markers in setState to reflect state changes."
        },
        {
            "instruction": "How do you implement role-based access control in Flutter?",
            "input": "",
            "output": "RBAC checks user roles before showing UI or allowing actions. Store role in user model from backend JWT. Create a permission service: class PermissionService { bool canEdit(User user) => user.role == Role.admin || user.role == Role.editor; }. Conditionally show widgets: if (permService.canEdit(user)) EditButton(). Use route guards to prevent navigation to unauthorized screens. Validate permissions server-side too."
        },
        {
            "instruction": "How do you implement image compression in Flutter?",
            "input": "",
            "output": "Image compression uses flutter_image_compress: final result = await FlutterImageCompress.compressWithFile(path, quality: 70, minWidth: 1024). For in-memory: compressWithList(bytes). Reduces file size significantly for upload. Alternative: image package for manual resize/crop. Set quality 70-85 for good balance. Compare compressed vs original size. Compress before uploading to save bandwidth."
        },
        {
            "instruction": "How do you implement app shortcuts (quick actions) in Flutter?",
            "input": "",
            "output": "App shortcuts use quick_actions package. Define shortcuts: QuickActions().setShortcutItems([ShortcutItem(type: 'search', localizedTitle: 'Search', icon: 'search_icon')]). Handle: QuickActions().initialize((type) { if (type == 'search') navigateToSearch(); }). On Android these appear as App Shortcuts (long press), on iOS as 3D Touch/Haptic Touch actions. Limited to 4 shortcuts."
        },
        {
            "instruction": "How do you implement text-to-speech and speech-to-text in Flutter?",
            "input": "",
            "output": "Text-to-speech: flutter_tts package. await flutterTts.speak('Hello'); Set language: setLanguage('en-US'), rate: setSpeechRate(0.5), pitch: setPitch(1.0). Speech-to-text: speech_to_text package. Initialize, then listen: stt.listen(onResult: (result) { text = result.recognizedWords; }). Check stt.isAvailable. Handle permissions for microphone access."
        },
        {
            "instruction": "How do you implement WebSocket communication in Flutter?",
            "input": "",
            "output": "WebSocket uses web_socket_channel package: final channel = WebSocketChannel.connect(Uri.parse('wss://echo.websocket.org')). Send: channel.sink.add('message'). Receive: StreamBuilder(stream: channel.stream, builder: ...). Close: channel.sink.close(). Handle reconnection on disconnect with retry logic. Use IOWebSocketChannel for dart:io or HtmlWebSocketChannel for web. JSON encode/decode messages."
        },
        {
            "instruction": "How do you implement app badges and notification counts?",
            "input": "",
            "output": "App badges on the app icon use flutter_app_badger: FlutterAppBadger.updateBadgeCount(5). Remove: removeBadge(). Check support: isAppBadgeSupported(). For in-app badges, use the Badge widget (Material 3): Badge(label: Text('3'), child: Icon(Icons.mail)). Position with Stack and Positioned for custom badge placement. Update count from notification data or API."
        },
        {
            "instruction": "How do you implement a color picker in Flutter?",
            "input": "",
            "output": "Color picker uses the flutter_colorpicker package. showDialog with ColorPicker widget: ColorPicker(pickerColor: currentColor, onColorChanged: (color) { setState(() => selectedColor = color); }). Block, material, and ring picker styles available. For simpler selection, use a GridView of predefined color swatches. Save selected color as int value with color.value."
        },
        {
            "instruction": "How do you implement horizontal scrollable tabs?",
            "input": "",
            "output": "Horizontal tabs use TabBar with TabController and isScrollable: true for many tabs. Each tab can be a Tab(text:) or Tab(child: customWidget). TabBarView provides the tab content. For non-TabBar scrollable chips, use a horizontal ListView or SingleChildScrollView with Row of FilterChips. Default TabBar clips to screen width; isScrollable lets tabs scroll horizontally."
        },
        {
            "instruction": "How do you implement background fetch in Flutter?",
            "input": "",
            "output": "Background fetch uses background_fetch or workmanager packages. workmanager: Workmanager().registerOneOffTask('task1', 'simpleTask') or registerPeriodicTask for recurring. Define callbackDispatcher as top-level function. On iOS, register BGTaskScheduler capabilities. On Android, uses WorkManager API. Constraints: requiresNetworkConnectivity, requiresCharging. Background execution is limited by OS energy management."
        },
        {
            "instruction": "How do you implement in-app purchase in Flutter?",
            "input": "",
            "output": "In-app purchases use the in_app_purchase package (official Flutter plugin). Query products: await InAppPurchase.instance.queryProductDetails({'product_id'}). Buy: InAppPurchase.instance.buyConsumable(purchaseParam: param). Listen to purchaseStream for purchase updates. Verify receipts server-side. Handle pending, purchased, error, and restored states. Configure products in App Store Connect and Google Play Console."
        },
        {
            "instruction": "How do you implement Hive database operations in Flutter?",
            "input": "",
            "output": "Hive is a lightweight NoSQL database. Initialize: await Hive.initFlutter(). Register adapters for custom objects: Hive.registerAdapter(UserAdapter()). Open box: var box = await Hive.openBox('users'). CRUD: box.put('key', user), box.get('key'), box.delete('key'), box.values, box.toMap(). Use @HiveType and @HiveField annotations with hive_generator for type adapters. Hive is fast and doesn't need native dependencies."
        },
        {
            "instruction": "How do you implement custom transitions with GoRouter?",
            "input": "",
            "output": "GoRouter custom transitions use pageBuilder instead of builder: GoRoute(path: '/detail', pageBuilder: (context, state) => CustomTransitionPage(child: DetailScreen(), transitionsBuilder: (context, animation, secondaryAnimation, child) => FadeTransition(opacity: animation, child: child), transitionDuration: Duration(milliseconds: 300))). Apply SlideTransition, ScaleTransition, or combine multiple effects."
        },
        {
            "instruction": "How do you implement a sticky header list in Flutter?",
            "input": "",
            "output": "Sticky headers use CustomScrollView with SliverPersistentHeader or SliverAppBar(pinned: true). For grouped lists with sticky section headers, use SliverStickyHeader from flutter_sticky_header package. Or implement manually with SliverPersistentHeader(delegate: MyDelegate(), pinned: true). Each section has a pinned header and SliverList of items. Headers stick at top while scrolling their section."
        },
        {
            "instruction": "How do you implement form autofill in Flutter?",
            "input": "",
            "output": "Form autofill uses AutofillGroup wrapping TextFormFields with autofillHints: AutofillGroup(child: Column(children: [TextFormField(autofillHints: [AutofillHints.email]), TextFormField(autofillHints: [AutofillHints.password])])). Call TextInput.finishAutofillContext() on form submit. Supports email, password, name, phone, address autofill. Works with platform password managers and browser autofill on web."
        },
        # --- Additional Intermediate Questions ---
        # Networking & APIs
        {
            "instruction": "How do you handle API pagination in Flutter?",
            "input": "",
            "output": "API pagination patterns: 1) Offset-based: fetch items with ?page=2&limit=20, track currentPage. 2) Cursor-based: use ?cursor=abc123 from response's nextCursor. 3) Implement with ScrollController: controller.addListener(() { if (controller.position.pixels >= controller.position.maxScrollExtent - 200) loadMore(); }). 4) Maintain isLoading flag to prevent duplicate requests. 5) Append new items to existing list. 6) Show loading indicator at bottom. Use infinite_scroll_pagination package for built-in support."
        },
        {
            "instruction": "How do you implement retry logic for failed HTTP requests in Flutter?",
            "input": "",
            "output": "Retry logic approaches: 1) Manual: wrap request in loop with try/catch, add delay between retries using Future.delayed. 2) Exponential backoff: delay = baseDelay * pow(2, attempt). 3) Use dio's interceptors: class RetryInterceptor extends Interceptor { onError(err, handler) { if (retryCount < maxRetries) { dio.fetch(err.requestOptions); } } }. 4) http_retry package wraps http.Client with automatic retries. 5) Set maxRetries, backoff factor, and retryable status codes (500, 502, 503)."
        },
        {
            "instruction": "How do you upload files with multipart requests in Flutter?",
            "input": "",
            "output": "File upload with http package: var request = http.MultipartRequest('POST', Uri.parse(url)); request.files.add(await http.MultipartFile.fromPath('file', filePath)); request.fields['name'] = 'test'; var response = await request.send();. With Dio: FormData formData = FormData.fromMap({'file': await MultipartFile.fromFile(path, filename: 'upload.jpg')}); dio.post(url, data: formData, onSendProgress: (sent, total) => print('${sent/total}'));. Track progress with onSendProgress callback."
        },
        {
            "instruction": "How do you handle WebSocket connections in Flutter?",
            "input": "",
            "output": "WebSocket usage: final channel = WebSocketChannel.connect(Uri.parse('wss://example.com/ws'));. Send: channel.sink.add('message');. Receive: StreamBuilder(stream: channel.stream, builder: (context, snapshot) => Text(snapshot.data ?? ''));. Close: channel.sink.close(). Use web_socket_channel package. Handle reconnection with Timer on close. For complex cases, use socket_io_client package. Always dispose channel in dispose() method."
        },
        {
            "instruction": "How do you implement GraphQL queries in Flutter?",
            "input": "",
            "output": "Use graphql_flutter package. Setup: GraphQLProvider(client: ValueNotifier(GraphQLClient(link: HttpLink('https://api.example.com/graphql'), cache: GraphQLCache())), child: MyApp()). Query: Query(options: QueryOptions(document: gql(queryString)), builder: (result, {fetchMore, refetch}) { if (result.isLoading) return CircularProgressIndicator(); return ListView(...); }). Mutations: Mutation widget with onCompleted callback. Supports caching, optimistic updates, subscriptions."
        },
        {
            "instruction": "How do you cancel HTTP requests in Flutter?",
            "input": "",
            "output": "With Dio: use CancelToken. var cancelToken = CancelToken(); dio.get(url, cancelToken: cancelToken); cancelToken.cancel('User cancelled');. With http package: create a client and close it: var client = http.Client(); var response = await client.get(url); client.close();. Cancel on widget dispose. For search-as-you-type, cancel previous request before making new one. Check CancelToken.isCancel(error) to distinguish cancellation from real errors."
        },
        {
            "instruction": "How do you implement certificate pinning in Flutter?",
            "input": "",
            "output": "Certificate pinning prevents MITM attacks. With Dio: (dio.httpClientAdapter as DefaultHttpClientAdapter).onHttpClientCreate = (client) { client.badCertificateCallback = (cert, host, port) { return cert.pem == expectedPem; }; return client; };. With http: use SecurityContext()..setTrustedCertificatesBytes(certBytes). For easier setup, use dio_http2_adapter or flutter_sslpinning_plugin. Pin the leaf certificate or public key hash. Rotate pins before cert expiry."
        },
        # Animations
        {
            "instruction": "How do you create a page transition animation in Flutter?",
            "input": "",
            "output": "Custom page transitions: Navigator.push(context, PageRouteBuilder(pageBuilder: (context, animation, secondaryAnimation) => NewPage(), transitionsBuilder: (context, animation, secondaryAnimation, child) { var tween = Tween(begin: Offset(1.0, 0.0), end: Offset.zero).chain(CurveTween(curve: Curves.easeInOut)); return SlideTransition(position: animation.drive(tween), child: child); }, transitionDuration: Duration(milliseconds: 500)));. Built-in: MaterialPageRoute, CupertinoPageRoute."
        },
        {
            "instruction": "How do you use AnimationController in Flutter?",
            "input": "",
            "output": "AnimationController drives animations over a duration. Requires SingleTickerProviderStateMixin (or TickerProviderStateMixin for multiple). late AnimationController _controller = AnimationController(vsync: this, duration: Duration(seconds: 1));. Control: _controller.forward(), .reverse(), .repeat(), .stop(), .reset(). Value ranges 0.0 to 1.0 by default. Add listeners with addListener() for rebuilds, addStatusListener() for completion events. Always dispose in dispose()."
        },
        {
            "instruction": "How do you create staggered animations in Flutter?",
            "input": "",
            "output": "Staggered animations use Interval with a single AnimationController. Each element animates at different time intervals: final slideAnimation = Tween(begin: Offset(-1, 0), end: Offset.zero).animate(CurvedAnimation(parent: _controller, curve: Interval(0.0, 0.4, curve: Curves.ease))); final fadeAnimation = Tween(begin: 0.0, end: 1.0).animate(CurvedAnimation(parent: _controller, curve: Interval(0.2, 0.6, curve: Curves.ease)));. Intervals are fractions (0.0-1.0) of total duration. Use AnimatedBuilder to rebuild."
        },
        {
            "instruction": "How do you animate a list item addition/removal in Flutter?",
            "input": "",
            "output": "Use AnimatedList for animated insertions/removals. final _listKey = GlobalKey<AnimatedListState>();. Insert: _listKey.currentState?.insertItem(index, duration: Duration(milliseconds: 300));. Remove: _listKey.currentState?.removeItem(index, (context, animation) => SizeTransition(sizeFactor: animation, child: removedItemWidget));. Build items with SlideTransition, FadeTransition, or SizeTransition wrapping animation parameter. Also consider AnimatedSwitcher for swapping single widgets."
        },
        {
            "instruction": "What is the Hero widget and how does it work?",
            "input": "",
            "output": "Hero creates a shared element transition between screens. Wrap the widget on both source and destination with Hero(tag: 'uniqueTag', child: Image(...)). Tags must match on both screens. During navigation, Flutter automatically animates the widget flying between positions. Works with Navigator.push. Customize with flightShuttleBuilder for intermediate appearance, placeholderBuilder during flight. Use createRectTween for custom flight paths."
        },
        {
            "instruction": "How do you use TweenAnimationBuilder in Flutter?",
            "input": "",
            "output": "TweenAnimationBuilder is an implicit animation for custom values. TweenAnimationBuilder<double>(tween: Tween(begin: 0, end: 1), duration: Duration(seconds: 1), builder: (context, value, child) { return Opacity(opacity: value, child: child); }, child: Text('Hello'), onEnd: () => print('done')). Works with any Tween type (Color, Offset, double). Automatically animates when tween end value changes. Simpler than AnimationController for one-off animations."
        },
        {
            "instruction": "How do you create a custom Tween in Flutter?",
            "input": "",
            "output": "Extend Tween<T> and override lerp(): class SizeTween extends Tween<Size> { SizeTween({required Size begin, required Size end}) : super(begin: begin, end: end); @override Size lerp(double t) { return Size(lerpDouble(begin!.width, end!.width, t)!, lerpDouble(begin!.height, end!.height, t)!); } }. Use with AnimationController: _animation = SizeTween(begin: Size(0, 0), end: Size(100, 100)).animate(_controller);. Custom tweens enable smooth interpolation of any data type."
        },
        {
            "instruction": "How do you implement physics-based animations in Flutter?",
            "input": "",
            "output": "Physics simulations create natural motion. Use SpringSimulation: final spring = SpringDescription(mass: 1, stiffness: 100, damping: 10); _controller.animateWith(SpringSimulation(spring, 0, 1, velocity));. GravitySimulation for falling: _controller.animateWith(GravitySimulation(200, 0, 300, 0));. FrictionSimulation for deceleration. ClampingScrollSimulation for fling-to-stop. Physics animations have no fixed duration — they complete based on physics parameters."
        },
        # UI Patterns
        {
            "instruction": "How do you implement a bottom sheet in Flutter?",
            "input": "",
            "output": "Modal bottom sheet: showModalBottomSheet(context: context, isScrollControlled: true, shape: RoundedRectangleBorder(borderRadius: BorderRadius.vertical(top: Radius.circular(20))), builder: (context) => Container(padding: EdgeInsets.all(16), child: Column(...))); Persistent: Scaffold.bottomSheet or showBottomSheet(). Use DraggableScrollableSheet for draggable resizable sheets. Set isScrollControlled: true for full-height sheets. Dismiss with Navigator.pop()."
        },
        {
            "instruction": "How do you implement a search bar with suggestions in Flutter?",
            "input": "",
            "output": "Use SearchDelegate: class MySearchDelegate extends SearchDelegate { @override List<Widget> buildActions(context) => [IconButton(icon: Icon(Icons.clear), onPressed: () => query = '')]; @override Widget buildLeading(context) => BackButton(onPressed: () => close(context, null)); @override Widget buildResults(context) => ResultsList(query); @override Widget buildSuggestions(context) => SuggestionsList(query); }. Show with: showSearch(context: context, delegate: MySearchDelegate());. Also use SearchAnchor in Material 3."
        },
        {
            "instruction": "How do you create a custom dialog in Flutter?",
            "input": "",
            "output": "showDialog(context: context, barrierDismissible: false, builder: (context) => Dialog(shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)), child: Padding(padding: EdgeInsets.all(20), child: Column(mainAxisSize: MainAxisSize.min, children: [Text('Title'), SizedBox(height: 16), Text('Content'), SizedBox(height: 24), Row(mainAxisAlignment: MainAxisAlignment.end, children: [TextButton(onPressed: () => Navigator.pop(context), child: Text('Cancel')), ElevatedButton(onPressed: () => Navigator.pop(context, true), child: Text('OK'))])]))));. Use AlertDialog for standard dialogs."
        },
        {
            "instruction": "How do you implement a tab bar in Flutter?",
            "input": "",
            "output": "Use DefaultTabController with TabBar and TabBarView. DefaultTabController(length: 3, child: Scaffold(appBar: AppBar(bottom: TabBar(tabs: [Tab(text: 'Tab 1'), Tab(icon: Icon(Icons.star)), Tab(text: 'Tab 3')])), body: TabBarView(children: [Page1(), Page2(), Page3()]))); For custom control: create TabController with SingleTickerProviderStateMixin. Listen to changes: _tabController.addListener(() { if (!_tabController.indexIsChanging) { ... } });. Customize with indicatorColor, labelColor, unselectedLabelColor."
        },
        {
            "instruction": "How do you implement pull-to-refresh in Flutter?",
            "input": "",
            "output": "Wrap scrollable widget with RefreshIndicator: RefreshIndicator(onRefresh: () async { await fetchData(); setState(() {}); }, child: ListView.builder(...));. The onRefresh callback must return a Future. Customize: color (spinner color), backgroundColor, displacement (trigger distance), strokeWidth. For CustomScrollView: use CupertinoSliverRefreshControl for iOS-style. The child must be a scrollable widget (ListView, GridView, CustomScrollView)."
        },
        {
            "instruction": "How do you implement a shimmer loading effect in Flutter?",
            "input": "",
            "output": "Use shimmer package: Shimmer.fromColors(baseColor: Colors.grey[300]!, highlightColor: Colors.grey[100]!, child: Column(children: [Container(height: 20, width: double.infinity, color: Colors.white), SizedBox(height: 8), Container(height: 20, width: 200, color: Colors.white)]));. Create placeholder widgets matching content layout. Show shimmer while isLoading is true, swap to real content when data loads. Custom shimmer: use LinearGradient with AnimationController for the sweep effect."
        },
        {
            "instruction": "How do you create a stepper form in Flutter?",
            "input": "",
            "output": "Stepper(currentStep: _currentStep, onStepContinue: () { if (_currentStep < steps.length - 1) setState(() => _currentStep++); }, onStepCancel: () { if (_currentStep > 0) setState(() => _currentStep--); }, steps: [Step(title: Text('Personal'), content: TextFormField(...), isActive: _currentStep >= 0), Step(title: Text('Address'), content: TextFormField(...), isActive: _currentStep >= 1)]);. Types: StepperType.vertical (default), StepperType.horizontal. Validate before continuing with Form key."
        },
        {
            "instruction": "How do you create a drawer menu in Flutter?",
            "input": "",
            "output": "Scaffold(drawer: Drawer(child: ListView(padding: EdgeInsets.zero, children: [DrawerHeader(decoration: BoxDecoration(color: Colors.blue), child: Text('Menu', style: TextStyle(color: Colors.white))), ListTile(leading: Icon(Icons.home), title: Text('Home'), onTap: () { Navigator.pop(context); Navigator.pushNamed(context, '/home'); }), ListTile(leading: Icon(Icons.settings), title: Text('Settings'), onTap: () {})])));. Open programmatically: Scaffold.of(context).openDrawer(). Use endDrawer for right-side drawer."
        },
        {
            "instruction": "How do you implement a tooltip in Flutter?",
            "input": "",
            "output": "Tooltip(message: 'This is a tooltip', child: IconButton(icon: Icon(Icons.info), onPressed: () {}));. Customize: height, padding, margin, verticalOffset, preferBelow, textStyle, decoration, waitDuration (delay before showing), showDuration (auto-hide delay). For rich tooltips: use Tooltip with richMessage parameter taking InlineSpan. Long-press or hover (desktop) triggers display. Material 3 uses textAlign and decoration for styling."
        },
        {
            "instruction": "How do you implement a snackbar in Flutter?",
            "input": "",
            "output": "ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Message'), action: SnackBarAction(label: 'Undo', onPressed: () {}), duration: Duration(seconds: 3), behavior: SnackBarBehavior.floating, shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)), margin: EdgeInsets.all(16)));. Use ScaffoldMessenger (not Scaffold.of) for reliable display across navigation. Hide: ScaffoldMessenger.of(context).hideCurrentSnackBar(). Floating behavior detaches from bottom edge."
        },
        {
            "instruction": "How do you implement a popup menu in Flutter?",
            "input": "",
            "output": "PopupMenuButton<String>(onSelected: (value) { print(value); }, itemBuilder: (context) => [PopupMenuItem(value: 'edit', child: ListTile(leading: Icon(Icons.edit), title: Text('Edit'))), PopupMenuItem(value: 'delete', child: ListTile(leading: Icon(Icons.delete), title: Text('Delete')))]);. Customize: icon, offset, shape, color, elevation. For contextual menus on long press, use showMenu(context: context, position: RelativeRect.fromLTRB(...), items: [...])."
        },
        {
            "instruction": "How do you implement a date/time picker in Flutter?",
            "input": "",
            "output": "Date picker: final date = await showDatePicker(context: context, initialDate: DateTime.now(), firstDate: DateTime(2000), lastDate: DateTime(2100));. Time picker: final time = await showTimePicker(context: context, initialTime: TimeOfDay.now());. Date range: showDateRangePicker(). Customize with builder parameter for themes. Use CupertinoDatePicker for iOS style inside showModalBottomSheet. Format with intl package: DateFormat('yyyy-MM-dd').format(date)."
        },
        {
            "instruction": "How do you implement an expandable list tile in Flutter?",
            "input": "",
            "output": "ExpansionTile(title: Text('Category'), subtitle: Text('Tap to expand'), leading: Icon(Icons.category), children: [ListTile(title: Text('Item 1')), ListTile(title: Text('Item 2'))], initiallyExpanded: false, onExpansionChanged: (expanded) { print(expanded); });. For controlled expansion: use ExpansionPanelList with ExpansionPanel(headerBuilder: ..., body: ..., isExpanded: _expanded). AnimatedContainer or AnimatedCrossFade for custom expandable widgets."
        },
        # Data Persistence
        {
            "instruction": "How do you use SharedPreferences in Flutter?",
            "input": "",
            "output": "SharedPreferences stores key-value pairs persistently. Setup: final prefs = await SharedPreferences.getInstance();. Write: await prefs.setString('name', 'John'); await prefs.setInt('age', 25); await prefs.setBool('loggedIn', true); await prefs.setStringList('tags', ['a', 'b']);. Read: String? name = prefs.getString('name'); int? age = prefs.getInt('age');. Delete: await prefs.remove('name');. Clear all: await prefs.clear();. Not suitable for large data — use for simple settings and preferences."
        },
        {
            "instruction": "How do you implement SQLite database in Flutter?",
            "input": "",
            "output": "Use sqflite package. Open: final db = await openDatabase(join(await getDatabasesPath(), 'app.db'), version: 1, onCreate: (db, version) => db.execute('CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, age INTEGER)'));. Insert: await db.insert('users', {'name': 'John', 'age': 25});. Query: final users = await db.query('users', where: 'age > ?', whereArgs: [18]);. Update: await db.update('users', {'name': 'Jane'}, where: 'id = ?', whereArgs: [1]);. Delete: await db.delete('users', where: 'id = ?', whereArgs: [1]);. Use migrations for schema changes."
        },
        {
            "instruction": "How do you use Hive for local storage in Flutter?",
            "input": "",
            "output": "Hive is a fast key-value database. Setup: await Hive.initFlutter(); var box = await Hive.openBox('settings');. Write: box.put('key', 'value'); box.putAll({'a': 1, 'b': 2});. Read: var val = box.get('key', defaultValue: 'default');. Delete: box.delete('key');. For custom objects: extend HiveObject with @HiveType, @HiveField annotations. Register adapter: Hive.registerAdapter(UserAdapter());. Encrypted box: Hive.openBox('secure', encryptionCipher: HiveAesCipher(key));. Hive is synchronous for reads, async for writes."
        },
        {
            "instruction": "How do you implement file read/write operations in Flutter?",
            "input": "",
            "output": "Use path_provider and dart:io. Get directory: final dir = await getApplicationDocumentsDirectory();. Write: final file = File('${dir.path}/data.txt'); await file.writeAsString('Hello World');. Read: String content = await file.readAsString();. Binary: await file.writeAsBytes(bytes); Uint8List data = await file.readAsBytes();. Check exists: await file.exists();. Delete: await file.delete();. List files: Directory(dir.path).listSync(). Temporary files: getTemporaryDirectory(). Use streams for large files."
        },
        {
            "instruction": "How do you implement secure storage in Flutter?",
            "input": "",
            "output": "Use flutter_secure_storage for sensitive data like tokens. final storage = FlutterSecureStorage();. Write: await storage.write(key: 'token', value: 'abc123');. Read: String? token = await storage.read(key: 'token');. Delete: await storage.delete(key: 'token');. Delete all: await storage.deleteAll();. Contains: bool has = await storage.containsKey(key: 'token');. Uses Keychain on iOS, EncryptedSharedPreferences on Android. Better than SharedPreferences for passwords, API keys, auth tokens."
        },
        {
            "instruction": "How do you cache API responses locally in Flutter?",
            "input": "",
            "output": "Caching strategies: 1) dio_cache_interceptor with Dio for HTTP-level caching with configurable policies. 2) Manual: store JSON in SharedPreferences/Hive with timestamp, check if expired before API call. 3) Repository pattern: class UserRepo { Future<List<User>> getUsers() async { final cached = await _cache.get('users'); if (cached != null && !isExpired(cached.timestamp)) return cached.data; final data = await api.fetchUsers(); await _cache.set('users', data); return data; } }. 4) Cache-first, network-first, or stale-while-revalidate strategies."
        },
        # Routing & Navigation
        {
            "instruction": "How do you pass data between screens in Flutter?",
            "input": "",
            "output": "Methods: 1) Constructor: Navigator.push(context, MaterialPageRoute(builder: (_) => DetailScreen(item: myItem)));. 2) Arguments: Navigator.pushNamed(context, '/detail', arguments: myItem); retrieve with ModalRoute.of(context)!.settings.arguments. 3) Return data: final result = await Navigator.push(context, route); in second screen: Navigator.pop(context, resultData);. 4) With GoRouter: context.go('/detail', extra: myItem);. 5) State management: read from provider/bloc on destination screen."
        },
        {
            "instruction": "How do you implement deep linking in Flutter?",
            "input": "",
            "output": "Deep linking opens specific app screens from URLs. Setup: 1) Android: add intent-filter in AndroidManifest.xml with scheme, host, pathPrefix. 2) iOS: add Associated Domains in Runner.entitlements and apple-app-site-association on server. 3) In Flutter: use GoRouter with routes matching URL patterns. GoRouter(routes: [GoRoute(path: '/product/:id', builder: (context, state) => ProductScreen(id: state.pathParameters['id']!))]). Verify with: adb shell am start -a android.intent.action.VIEW -d 'https://example.com/product/123'."
        },
        {
            "instruction": "How do you implement nested navigation in Flutter?",
            "input": "",
            "output": "Nested navigation uses multiple Navigators. Each section has its own Navigator with a unique key: BottomNavigationBar + IndexedStack of Navigator widgets. Navigator(key: _tab1NavKey, onGenerateRoute: ...). This preserves each tab's navigation stack. With GoRouter: ShellRoute(builder: (context, state, child) => ScaffoldWithNavBar(child: child), routes: [GoRoute(path: '/home', builder: ...), GoRoute(path: '/settings', builder: ...)]);. Use parentNavigatorKey to control which navigator handles a route."
        },
        {
            "instruction": "How do you implement route guards/authentication in navigation?",
            "input": "",
            "output": "Route guards redirect unauthenticated users. GoRouter: GoRouter(redirect: (context, state) { final isLoggedIn = authService.isLoggedIn; final isLoginRoute = state.matchedLocation == '/login'; if (!isLoggedIn && !isLoginRoute) return '/login'; if (isLoggedIn && isLoginRoute) return '/home'; return null; // no redirect }, routes: [...]);. With Navigator 2.0: override RouteInformationParser to check auth state. Common pattern: listen to auth state stream and trigger redirect on changes."
        },
        {
            "instruction": "How do you implement bottom navigation with persistent state?",
            "input": "",
            "output": "Use IndexedStack to preserve tab state: int _selectedIndex = 0; Scaffold(body: IndexedStack(index: _selectedIndex, children: [HomeTab(), SearchTab(), ProfileTab()]), bottomNavigationBar: BottomNavigationBar(currentIndex: _selectedIndex, onTap: (index) => setState(() => _selectedIndex = index), items: [...]));. IndexedStack keeps all children alive but only shows the selected one. Alternative: AutomaticKeepAliveClientMixin with PageView. With GoRouter: use StatefulShellRoute for persistent shell state."
        },
        # State Management
        {
            "instruction": "How does Provider state management work in Flutter?",
            "input": "",
            "output": "Provider uses InheritedWidget for dependency injection and state management. Setup: 1) Create ChangeNotifier: class Counter extends ChangeNotifier { int _count = 0; int get count => _count; void increment() { _count++; notifyListeners(); } }. 2) Provide: ChangeNotifierProvider(create: (_) => Counter(), child: MyApp()). 3) Consume: Consumer<Counter>(builder: (context, counter, child) => Text('${counter.count}')) or context.watch<Counter>().count. Use context.read<Counter>() for one-time access without rebuilds."
        },
        {
            "instruction": "What is the difference between context.watch and context.read in Provider?",
            "input": "",
            "output": "context.watch<T>() listens to changes and rebuilds the widget when the value changes. Use in build() method. context.read<T>() accesses the value once without subscribing to changes. Use in callbacks like onPressed. context.select<T, R>((T value) => value.property) watches only a specific property, preventing unnecessary rebuilds. Rule: watch in build, read in events. Using read in build won't update UI; using watch in callbacks is wasteful."
        },
        {
            "instruction": "How do you implement Riverpod state management?",
            "input": "",
            "output": "Riverpod is a compile-safe Provider replacement. Setup: wrap app in ProviderScope(child: MyApp()). Define providers: final counterProvider = StateNotifierProvider<CounterNotifier, int>((ref) => CounterNotifier()); class CounterNotifier extends StateNotifier<int> { CounterNotifier() : super(0); void increment() => state++; }. Consume in ConsumerWidget: ref.watch(counterProvider) for reactive UI, ref.read(counterProvider.notifier).increment() for actions. Providers: Provider, StateProvider, FutureProvider, StreamProvider, StateNotifierProvider."
        },
        {
            "instruction": "How do you implement GetX state management?",
            "input": "",
            "output": "GetX offers reactive state, dependency injection, and routing. Controller: class CounterController extends GetxController { var count = 0.obs; void increment() => count++; }. Inject: Get.put(CounterController());. Consume: Obx(() => Text('${controller.count}')). Navigation: Get.to(NextPage()), Get.toNamed('/next'). Snackbar: Get.snackbar('Title', 'Message'). Dialog: Get.dialog(AlertDialog(...)). GetX is criticized for tight coupling but praised for rapid development. Use GetBuilder for non-reactive rebuilds."
        },
        {
            "instruction": "How do you use ValueNotifier and ValueListenableBuilder?",
            "input": "",
            "output": "ValueNotifier holds a single value and notifies listeners on change. final counter = ValueNotifier<int>(0);. Increment: counter.value++;. Listen in UI: ValueListenableBuilder<int>(valueListenable: counter, builder: (context, value, child) => Text('$value'), child: Icon(Icons.star));. The child parameter is optimization — it's not rebuilt. Simpler than ChangeNotifier for single values. Dispose in dispose(): counter.dispose();. Use for simple local state without full state management packages."
        },
        # Responsive Design
        {
            "instruction": "How do you create a responsive layout in Flutter?",
            "input": "",
            "output": "Responsive approaches: 1) MediaQuery: var width = MediaQuery.of(context).size.width; if (width > 600) showTabletLayout(); 2) LayoutBuilder: LayoutBuilder(builder: (context, constraints) { if (constraints.maxWidth > 900) return WideLayout(); return NarrowLayout(); }). 3) Flexible/Expanded for proportional sizing. 4) AspectRatio widget. 5) FractionallySizedBox for percentage-based sizing. 6) OrientationBuilder for portrait/landscape. 7) responsive_framework or flutter_screenutil packages for breakpoint-based layouts."
        },
        {
            "instruction": "How do you handle different screen orientations in Flutter?",
            "input": "",
            "output": "Lock orientation: SystemChrome.setPreferredOrientations([DeviceOrientation.portraitUp, DeviceOrientation.portraitDown]);. Detect: OrientationBuilder(builder: (context, orientation) { return orientation == Orientation.portrait ? PortraitLayout() : LandscapeLayout(); });. Or: MediaQuery.of(context).orientation. Per-screen lock: set in initState, reset in dispose. Handle keyboard affecting layout: MediaQuery.of(context).viewInsets.bottom > 0 detects keyboard open."
        },
        {
            "instruction": "How do you implement adaptive widgets for different platforms?",
            "input": "",
            "output": "Use Platform-adaptive widgets: 1) Check platform: import 'dart:io'; if (Platform.isIOS) CupertinoButton(...) else ElevatedButton(...). 2) .adaptive constructors: Switch.adaptive(), Slider.adaptive(), CircularProgressIndicator.adaptive() automatically use Cupertino on iOS. 3) Use Theme.of(context).platform for platform-aware theming. 4) flutter_platform_widgets package provides PlatformWidget, PlatformApp, PlatformScaffold that auto-switch. 5) TargetPlatform enum for desktop platforms."
        },
        # Forms & Input
        {
            "instruction": "How do you implement form validation in Flutter?",
            "input": "",
            "output": "Use Form with GlobalKey<FormState>. final _formKey = GlobalKey<FormState>();. Form(key: _formKey, child: Column(children: [TextFormField(validator: (value) { if (value == null || value.isEmpty) return 'Required'; if (value.length < 3) return 'Too short'; return null; })]));. Validate: if (_formKey.currentState!.validate()) { _formKey.currentState!.save(); // process data }. AutovalidateMode.onUserInteraction for real-time validation. Custom validators: email regex, password strength, matching fields."
        },
        {
            "instruction": "How do you handle text input formatting in Flutter?",
            "input": "",
            "output": "TextFormField(inputFormatters: [FilteringTextInputFormatter.digitsOnly, LengthLimitingTextInputFormatter(10), FilteringTextInputFormatter.allow(RegExp(r'[a-zA-Z]'))]);. Custom formatter: class PhoneFormatter extends TextInputFormatter { @override TextEditingValue formatEditUpdate(old, new_) { // format as (123) 456-7890 } }. Use keyboardType: TextInputType.number for numeric keyboard. mask_text_input_formatter package for patterns like ##/##/####."
        },
        {
            "instruction": "How do you create a multi-step form wizard in Flutter?",
            "input": "",
            "output": "Multi-step form using PageView: PageView(controller: _pageController, physics: NeverScrollableScrollPhysics(), children: [Step1Form(data: _formData), Step2Form(data: _formData), Step3Review(data: _formData)]);. Navigation: _pageController.nextPage(duration: Duration(ms: 300), curve: Curves.ease). Validate each step before proceeding. Share form data via a data class or state management. Show progress with LinearProgressIndicator or Stepper. Save partial data for each step. Disable swipe with NeverScrollableScrollPhysics."
        },
        {
            "instruction": "How do you implement a dropdown form field in Flutter?",
            "input": "",
            "output": "DropdownButtonFormField<String>(value: selectedValue, decoration: InputDecoration(labelText: 'Category', border: OutlineInputBorder()), items: ['Option A', 'Option B', 'Option C'].map((e) => DropdownMenuItem(value: e, child: Text(e))).toList(), onChanged: (value) => setState(() => selectedValue = value), validator: (value) => value == null ? 'Please select' : null);. For searchable dropdown: use DropdownSearch from dropdown_search package. Customize icon, dropdownColor, isExpanded."
        },
        # Images & Media
        {
            "instruction": "How do you implement image picking from gallery/camera in Flutter?",
            "input": "",
            "output": "Use image_picker package. Pick from gallery: final XFile? image = await ImagePicker().pickImage(source: ImageSource.gallery, maxWidth: 800, maxHeight: 600, imageQuality: 85);. From camera: ImagePicker().pickImage(source: ImageSource.camera);. Multiple: ImagePicker().pickMultiImage(). Display: if (image != null) Image.file(File(image.path));. Add permissions: iOS Info.plist (NSCameraUsageDescription, NSPhotoLibraryUsageDescription), Android no extra permission needed for gallery."
        },
        {
            "instruction": "How do you implement image cropping in Flutter?",
            "input": "",
            "output": "Use image_cropper package. CroppedFile? croppedFile = await ImageCropper().cropImage(sourcePath: imageFile.path, aspectRatioPresets: [CropAspectRatioPreset.square, CropAspectRatioPreset.ratio16x9], uiSettings: [AndroidUiSettings(toolbarTitle: 'Crop', toolbarColor: Colors.blue, initAspectRatio: CropAspectRatioPreset.original, lockAspectRatio: false), IOsUiSettings(title: 'Crop')]);. Display: Image.file(File(croppedFile!.path)). Supports aspect ratio locking, rotation, custom UI."
        },
        {
            "instruction": "How do you implement video playback in Flutter?",
            "input": "",
            "output": "Use video_player package. Initialize: _controller = VideoPlayerController.networkUrl(Uri.parse(url))..initialize().then((_) => setState(() {}));. Play/pause: _controller.play(); _controller.pause();. UI: _controller.value.isInitialized ? AspectRatio(aspectRatio: _controller.value.aspectRatio, child: VideoPlayer(_controller)) : CircularProgressIndicator(). Seek: _controller.seekTo(Duration(seconds: 30)). Always dispose controller. Use chewie package for ready-made controls with progress bar."
        },
        {
            "instruction": "How do you implement SVG images in Flutter?",
            "input": "",
            "output": "Use flutter_svg package. SvgPicture.asset('assets/icon.svg', width: 50, height: 50, colorFilter: ColorFilter.mode(Colors.blue, BlendMode.srcIn));. From network: SvgPicture.network('https://example.com/icon.svg'). From string: SvgPicture.string(svgString). Benefits: resolution-independent, small file size, customizable colors. Declare SVG assets in pubspec.yaml. For complex SVGs, consider converting to custom paint or using cached rendering."
        },
        # Error Handling
        {
            "instruction": "How do you implement global error handling in Flutter?",
            "input": "",
            "output": "Global error handling: 1) Flutter errors: FlutterError.onError = (details) { FirebaseCrashlytics.instance.recordFlutterError(details); }. 2) Async errors: PlatformDispatcher.instance.onError = (error, stack) { logError(error, stack); return true; };. 3) Zone-based: runZonedGuarded(() => runApp(MyApp()), (error, stack) { reportError(error, stack); }). 4) Custom error widget: ErrorWidget.builder = (details) => CustomErrorWidget(details.exception.toString());. Combine all approaches in main()."
        },
        {
            "instruction": "How do you handle errors with Result types in Dart?",
            "input": "",
            "output": "Sealed class Result pattern: sealed class Result<T> {} class Success<T> extends Result<T> { final T data; Success(this.data); } class Failure<T> extends Result<T> { final String message; Failure(this.message); }. Usage: Future<Result<User>> getUser(int id) async { try { final user = await api.fetchUser(id); return Success(user); } catch (e) { return Failure(e.toString()); } }. Handle: switch(result) { case Success(:final data) => showUser(data), case Failure(:final message) => showError(message) }. Avoids throwing exceptions for expected failures."
        },
        # Platform Features
        {
            "instruction": "How do you implement push notifications in Flutter?",
            "input": "",
            "output": "Use firebase_messaging package. Setup: await Firebase.initializeApp(); final fcm = FirebaseMessaging.instance; await fcm.requestPermission();. Get token: String? token = await fcm.getToken();. Foreground: FirebaseMessaging.onMessage.listen((message) { showLocalNotification(message); });. Background: FirebaseMessaging.onBackgroundMessage(_handler); static Future<void> _handler(RemoteMessage message) async { }. Tap handling: FirebaseMessaging.onMessageOpenedApp.listen((message) => navigate(message.data));. Use flutter_local_notifications for display."
        },
        {
            "instruction": "How do you implement biometric authentication in Flutter?",
            "input": "",
            "output": "Use local_auth package. Check availability: final auth = LocalAuthentication(); bool canAuth = await auth.canCheckBiometrics; List<BiometricType> types = await auth.getAvailableBiometrics();. Authenticate: bool success = await auth.authenticate(localizedReason: 'Please authenticate', options: AuthenticationOptions(stickyAuth: true, biometricOnly: true));. Handle: if (success) grantAccess();. Add permissions: iOS Info.plist NSFaceIDUsageDescription, Android USE_BIOMETRIC permission. Supports fingerprint, face ID, iris."
        },
        {
            "instruction": "How do you implement in-app purchases in Flutter?",
            "input": "",
            "output": "Use in_app_purchase package. Initialize: final iap = InAppPurchase.instance; bool available = await iap.isAvailable();. Load products: final response = await iap.queryProductDetails({'product_id'});. Purchase: iap.buyConsumable(purchaseParam: PurchaseParam(productDetails: product));. Listen: iap.purchaseStream.listen((purchases) { for (var p in purchases) { if (p.status == PurchaseStatus.purchased) { verifyPurchase(p); iap.completePurchase(p); } } });. Always verify purchases server-side."
        },
        {
            "instruction": "How do you access device sensors in Flutter?",
            "input": "",
            "output": "Use sensors_plus package. Accelerometer: accelerometerEventStream().listen((event) { print('x: ${event.x}, y: ${event.y}, z: ${event.z}'); });. Gyroscope: gyroscopeEventStream().listen((event) { ... });. Magnetometer: magnetometerEventStream().listen((event) { ... });. For geolocation: geolocator package. For camera: camera package. For battery: battery_plus. All return streams — cancel subscriptions in dispose(). Use userAccelerometerEvents for gravity-filtered data."
        },
        {
            "instruction": "How do you implement app permissions in Flutter?",
            "input": "",
            "output": "Use permission_handler package. Check: var status = await Permission.camera.status; if (status.isDenied) { var result = await Permission.camera.request(); if (result.isGranted) { openCamera(); } }. Multiple: Map<Permission, PermissionStatus> statuses = await [Permission.camera, Permission.location].request();. Handle permanently denied: if (status.isPermanentlyDenied) openAppSettings();. Add actual permissions in AndroidManifest.xml and Info.plist. Check before using features, not at app start."
        },
        # Testing
        {
            "instruction": "How do you write unit tests in Flutter?",
            "input": "",
            "output": "Create test files in test/ directory with _test.dart suffix. import 'package:test/test.dart'; void main() { group('Calculator', () { test('adds two numbers', () { expect(Calculator().add(2, 3), equals(5)); }); test('throws on division by zero', () { expect(() => Calculator().divide(1, 0), throwsArgumentError); }); }); setUp(() { /* runs before each test */ }); tearDown(() { /* runs after each test */ }); }. Run: flutter test. Use mockito for mocking dependencies. AAA pattern: Arrange, Act, Assert."
        },
        {
            "instruction": "How do you write widget tests in Flutter?",
            "input": "",
            "output": "Widget tests verify UI behavior. testWidgets('counter increments', (tester) async { await tester.pumpWidget(MaterialApp(home: CounterPage())); expect(find.text('0'), findsOneWidget); await tester.tap(find.byIcon(Icons.add)); await tester.pump(); expect(find.text('1'), findsOneWidget); });. Finders: find.text(), find.byType(), find.byKey(), find.byIcon(). Actions: tester.tap(), tester.enterText(), tester.drag(), tester.longPress(). tester.pump() triggers rebuild, tester.pumpAndSettle() waits for animations."
        },
        {
            "instruction": "How do you mock dependencies in Flutter tests?",
            "input": "",
            "output": "Use mockito package. 1) Create mock: @GenerateMocks([ApiService]) import 'test.mocks.dart';. 2) Run build_runner: dart run build_runner build. 3) Use: final mockApi = MockApiService(); when(mockApi.fetchUser(1)).thenAnswer((_) async => User(name: 'Test')); final repo = UserRepo(api: mockApi); final user = await repo.getUser(1); expect(user.name, 'Test'); verify(mockApi.fetchUser(1)).called(1);. Stub errors: when(mock.method()).thenThrow(Exception()); Use any for argument matchers."
        },
        # Internationalization
        {
            "instruction": "How do you implement internationalization (i18n) in Flutter?",
            "input": "",
            "output": "Use flutter_localizations and intl packages. 1) Add to pubspec: flutter_localizations: sdk: flutter. 2) Configure MaterialApp: localizationsDelegates: [AppLocalizations.delegate, GlobalMaterialLocalizations.delegate, GlobalWidgetsLocalizations.delegate], supportedLocales: [Locale('en'), Locale('es')]. 3) Create ARB files: lib/l10n/app_en.arb with {\"hello\": \"Hello {name}\", \"@hello\": {\"placeholders\": {\"name\": {\"type\": \"String\"}}}}. 4) Generate: flutter gen-l10n. 5) Use: AppLocalizations.of(context)!.hello('World')."
        },
        {
            "instruction": "How do you handle RTL (right-to-left) layouts in Flutter?",
            "input": "",
            "output": "Flutter handles RTL automatically when locale is set to RTL language (Arabic, Hebrew). Force direction: Directionality(textDirection: TextDirection.rtl, child: MyWidget()). Use Directionality.of(context) to check. EdgeInsetsDirectional instead of EdgeInsets: EdgeInsetsDirectional.only(start: 16). AlignmentDirectional.centerStart instead of Alignment.centerLeft. Row automatically reverses children in RTL. Use TextDirection-aware properties: startMargin, endMargin. Test with: MaterialApp(locale: Locale('ar'))."
        },
        # Theming
        {
            "instruction": "How do you implement dark mode in Flutter?",
            "input": "",
            "output": "MaterialApp(theme: ThemeData.light(useMaterial3: true).copyWith(colorScheme: ColorScheme.fromSeed(seedColor: Colors.blue)), darkTheme: ThemeData.dark(useMaterial3: true).copyWith(colorScheme: ColorScheme.fromSeed(seedColor: Colors.blue, brightness: Brightness.dark)), themeMode: ThemeMode.system);. Override: themeMode: ThemeMode.dark. User preference: store in SharedPreferences, use Provider/ValueNotifier to toggle. Access current: Theme.of(context).brightness == Brightness.dark. Use ColorScheme tokens throughout for auto dark/light."
        },
        {
            "instruction": "How do you create a custom theme in Flutter?",
            "input": "",
            "output": "ThemeData(useMaterial3: true, colorScheme: ColorScheme.fromSeed(seedColor: Colors.indigo), textTheme: TextTheme(headlineLarge: TextStyle(fontSize: 32, fontWeight: FontWeight.bold), bodyMedium: TextStyle(fontSize: 16)), elevatedButtonTheme: ElevatedButtonThemeData(style: ElevatedButton.styleFrom(padding: EdgeInsets.symmetric(h: 24, v: 12))), inputDecorationTheme: InputDecorationTheme(border: OutlineInputBorder()), cardTheme: CardTheme(elevation: 2, shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12))));. Apply globally via MaterialApp(theme: myTheme)."
        },
        {
            "instruction": "How do you use custom fonts in Flutter?",
            "input": "",
            "output": "1) Add font files to assets/fonts/ directory. 2) Declare in pubspec.yaml: fonts: - family: MyFont; fonts: - asset: assets/fonts/MyFont-Regular.ttf; - asset: assets/fonts/MyFont-Bold.ttf; weight: 700; - asset: assets/fonts/MyFont-Italic.ttf; style: italic. 3) Use: TextStyle(fontFamily: 'MyFont', fontSize: 16). 4) Set globally: ThemeData(fontFamily: 'MyFont'). For Google Fonts: google_fonts package — Text('Hello', style: GoogleFonts.lato(fontSize: 20)). No asset declaration needed with google_fonts."
        },
        # Miscellaneous Intermediate
        {
            "instruction": "How do you implement clipboard operations in Flutter?",
            "input": "",
            "output": "Copy to clipboard: await Clipboard.setData(ClipboardData(text: 'Hello'));. Paste from clipboard: ClipboardData? data = await Clipboard.getData(Clipboard.kTextPlain); String? text = data?.text;. Show feedback: ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Copied!')));. For rich content, use super_clipboard package. Clipboard is from services library: import 'package:flutter/services.dart'."
        },
        {
            "instruction": "How do you implement app links and URL launching in Flutter?",
            "input": "",
            "output": "Use url_launcher package. Launch URL: final uri = Uri.parse('https://flutter.dev'); if (await canLaunchUrl(uri)) { await launchUrl(uri, mode: LaunchMode.externalApplication); }. Modes: externalApplication (browser), inAppWebView (in-app), platformDefault. Email: launchUrl(Uri(scheme: 'mailto', path: 'test@example.com', queryParameters: {'subject': 'Hello'})). Phone: launchUrl(Uri(scheme: 'tel', path: '+1234567890')). SMS: launchUrl(Uri(scheme: 'sms', path: '1234567890'))."
        },
        {
            "instruction": "How do you implement a splash screen in Flutter?",
            "input": "",
            "output": "Native splash (recommended): Use flutter_native_splash package. Create flutter_native_splash.yaml: color: '#42a5f5', image: assets/splash.png, android_12 settings. Run: dart run flutter_native_splash:create. For animated splash: Create a SplashScreen widget with AnimationController, show logo animation, then navigate: Future.delayed(Duration(seconds: 2), () => Navigator.pushReplacement(context, MaterialPageRoute(builder: (_) => HomeScreen())));. Remove native splash when Flutter renders: FlutterNativeSplash.remove()."
        },
        {
            "instruction": "How do you implement app versioning and build numbers in Flutter?",
            "input": "",
            "output": "Version is set in pubspec.yaml: version: 1.2.3+4 (semver+buildNumber). Access at runtime: import 'package:package_info_plus/package_info_plus.dart'; PackageInfo info = await PackageInfo.fromPlatform(); print(info.version); // 1.2.3 print(info.buildNumber); // 4. Override in build: flutter build apk --build-number=5 --build-name=1.2.4. Android: versionCode=buildNumber, versionName=version. iOS: CFBundleVersion=buildNumber, CFBundleShortVersionString=version."
        },
        {
            "instruction": "How do you implement connectivity checking in Flutter?",
            "input": "",
            "output": "Use connectivity_plus package. Check: final result = await Connectivity().checkConnectivity(); if (result == ConnectivityResult.mobile) { } else if (result == ConnectivityResult.wifi) { }. Listen for changes: Connectivity().onConnectivityChanged.listen((result) { updateUI(result); });. Note: connectivity_plus only checks network interface, not actual internet. For internet check: try { final response = await http.get(Uri.parse('https://google.com')); hasInternet = response.statusCode == 200; } catch (_) { hasInternet = false; }."
        },
        {
            "instruction": "How do you handle keyboard events in Flutter?",
            "input": "",
            "output": "Use RawKeyboardListener or KeyboardListener (newer): KeyboardListener(focusNode: _focusNode, onKeyEvent: (event) { if (event is KeyDownEvent && event.logicalKey == LogicalKeyboardKey.escape) { closeDialog(); } }, child: Focus(autofocus: true, child: MyWidget()));. For shortcuts: Shortcuts(shortcuts: {SingleActivator(LogicalKeyboardKey.keyS, control: true): SaveIntent()}, child: Actions(actions: {SaveIntent: CallbackAction(onInvoke: (_) => save())}, child: MyApp()));. Detect keyboard visibility: MediaQuery.of(context).viewInsets.bottom > 0."
        },
        {
            "instruction": "How do you implement drag and drop in Flutter?",
            "input": "",
            "output": "Use Draggable and DragTarget. Draggable<String>(data: 'item1', child: Chip(label: Text('Drag me')), feedback: Material(child: Chip(label: Text('Dragging'))), childWhenDragging: Opacity(opacity: 0.3, child: Chip(label: Text('Drag me'))));. DragTarget<String>(onAcceptWithDetails: (details) { setState(() => droppedItems.add(details.data)); }, builder: (context, candidateData, rejectedData) { return Container(color: candidateData.isNotEmpty ? Colors.green : Colors.grey); });. Use LongPressDraggable for long-press activation. ReorderableListView for list reordering."
        },
        {
            "instruction": "How do you implement custom painting in Flutter?",
            "input": "",
            "output": "Extend CustomPainter: class MyPainter extends CustomPainter { @override void paint(Canvas canvas, Size size) { final paint = Paint()..color = Colors.blue..style = PaintingStyle.fill; canvas.drawCircle(Offset(size.width/2, size.height/2), 50, paint); canvas.drawLine(Offset(0, 0), Offset(size.width, size.height), paint..strokeWidth = 2); final textPainter = TextPainter(text: TextSpan(text: 'Hi'), textDirection: TextDirection.ltr)..layout(); textPainter.paint(canvas, Offset(10, 10)); } @override bool shouldRepaint(old) => false; }. Use: CustomPaint(painter: MyPainter(), size: Size(200, 200))."
        },
        {
            "instruction": "How do you implement a countdown timer in Flutter?",
            "input": "",
            "output": "Using Timer.periodic: int _seconds = 60; Timer? _timer; void startTimer() { _timer = Timer.periodic(Duration(seconds: 1), (timer) { setState(() { if (_seconds > 0) _seconds--; else timer.cancel(); }); }); }. Display formatted: '${(_seconds ~/ 60).toString().padLeft(2, '0')}:${(_seconds % 60).toString().padLeft(2, '0')}'. Cancel in dispose(): _timer?.cancel(). Alternative: use CountdownTimer from quiver package or AnimationController with duration for visual countdown."
        },
        {
            "instruction": "How do you implement QR code scanning in Flutter?",
            "input": "",
            "output": "Use mobile_scanner package. MobileScanner(onDetect: (capture) { final List<Barcode> barcodes = capture.barcodes; for (final barcode in barcodes) { print('Barcode: ${barcode.rawValue}'); } });. Control camera: MobileScannerController controller = MobileScannerController(facing: CameraFacing.back, torchEnabled: false);. Toggle torch: controller.toggleTorch(). Switch camera: controller.switchCamera(). For generating QR codes: use qr_flutter package — QrImageView(data: 'hello', size: 200)."
        },
        {
            "instruction": "How do you implement local notifications in Flutter?",
            "input": "",
            "output": "Use flutter_local_notifications package. Initialize: final flnp = FlutterLocalNotificationsPlugin(); await flnp.initialize(InitializationSettings(android: AndroidInitializationSettings('@mipmap/ic_launcher'), iOS: DarwinInitializationSettings()));. Show: await flnp.show(0, 'Title', 'Body', NotificationDetails(android: AndroidNotificationDetails('channelId', 'channelName', importance: Importance.high)));. Schedule: flnp.zonedSchedule(0, 'Title', 'Body', scheduledDate, details, androidScheduleMode: AndroidScheduleMode.exactAllowWhileIdle, uiLocalNotificationDateInterpretation: UILocalNotificationDateInterpretation.absoluteTime)."
        },
        {
            "instruction": "How do you implement a map view in Flutter?",
            "input": "",
            "output": "Use google_maps_flutter package. GoogleMap(initialCameraPosition: CameraPosition(target: LatLng(37.7749, -122.4194), zoom: 14), markers: {Marker(markerId: MarkerId('1'), position: LatLng(37.7749, -122.4194), infoWindow: InfoWindow(title: 'SF'))}, onMapCreated: (controller) => _mapController = controller, myLocationEnabled: true, mapType: MapType.normal);. Add API key in AndroidManifest.xml and AppDelegate.swift. For OpenStreetMap: flutter_map package (no API key needed)."
        },
        {
            "instruction": "How do you implement charts and graphs in Flutter?",
            "input": "",
            "output": "Use fl_chart package. Line chart: LineChart(LineChartData(lineBarsData: [LineChartBarData(spots: [FlSpot(0, 3), FlSpot(1, 1), FlSpot(2, 4)], isCurved: true, color: Colors.blue)]));. Bar chart: BarChart(BarChartData(barGroups: [BarChartGroupData(x: 0, barRods: [BarChartRodData(toY: 8)])]));. Pie chart: PieChart(PieChartData(sections: [PieChartSectionData(value: 40, title: '40%', color: Colors.blue)]));. Alternative: syncfusion_flutter_charts for comprehensive charting."
        },
        {
            "instruction": "How do you implement PDF generation in Flutter?",
            "input": "",
            "output": "Use pdf package. final doc = pw.Document(); doc.addPage(pw.Page(build: (context) => pw.Column(children: [pw.Text('Report', style: pw.TextStyle(fontSize: 24, fontWeight: pw.FontWeight.bold)), pw.SizedBox(height: 20), pw.Table.fromTextArray(data: [['Name', 'Age'], ['John', '25']])]))); final bytes = await doc.save();. Save: final file = File('${dir.path}/report.pdf'); await file.writeAsBytes(bytes);. View: use open_file or printing package. printing package also supports direct print dialog."
        },
        {
            "instruction": "How do you implement audio playback in Flutter?",
            "input": "",
            "output": "Use audioplayers package. final player = AudioPlayer();. Play: await player.play(UrlSource('https://example.com/audio.mp3')); or AssetSource('audio.mp3');. Controls: player.pause(); player.resume(); player.stop(); player.seek(Duration(seconds: 30));. Listen: player.onDurationChanged.listen((d) {}); player.onPositionChanged.listen((p) {}); player.onPlayerComplete.listen((_) {});. Set volume: player.setVolume(0.5);. Dispose: player.dispose();. For recording: use record package."
        },
        {
            "instruction": "How do you implement background tasks in Flutter?",
            "input": "",
            "output": "Use workmanager package for periodic/one-off background tasks. Initialize: Workmanager().initialize(callbackDispatcher); void callbackDispatcher() { Workmanager().executeTask((task, inputData) async { await syncData(); return true; }); }. Register: Workmanager().registerOneOffTask('sync', 'syncTask', inputData: {'key': 'value'});. Periodic: Workmanager().registerPeriodicTask('periodic-sync', 'syncTask', frequency: Duration(hours: 1));. Constraints: NetworkType.connected, requiresBatteryNotLow, requiresCharging."
        },
        {
            "instruction": "How do you handle environment-specific configuration in Flutter?",
            "input": "",
            "output": "Using --dart-define: flutter run --dart-define=API_URL=https://api.dev.example.com. Access: const apiUrl = String.fromEnvironment('API_URL');. Multiple: use --dart-define-from-file=config.json. Alternative: create config classes per environment. Flavor-based: class AppConfig { static late String apiUrl; static void init(String env) { switch(env) { case 'dev': apiUrl = 'https://dev.api'; break; case 'prod': apiUrl = 'https://api'; break; } } }. Flutter flavors for distinct build configs: flutter run --flavor dev."
        },
        {
            "instruction": "How do you optimize ListView performance in Flutter?",
            "input": "",
            "output": "1) Use ListView.builder for lazy rendering — only builds visible items. 2) Add itemExtent or prototypeItem for fixed-height items — avoids layout calculation. 3) Use const constructors for list item widgets. 4) Add keys for proper widget reuse: Key(item.id). 5) Avoid heavy build methods — extract complex items to separate widgets. 6) Use RepaintBoundary to isolate repaints. 7) Cache computed values, don't compute in build(). 8) Use cacheExtent to pre-render items. 9) Paginate to limit data. 10) Profile with DevTools Timeline."
        },
        {
            "instruction": "How do you implement a custom scroll behavior in Flutter?",
            "input": "",
            "output": "Extend ScrollBehavior: class MyScrollBehavior extends ScrollBehavior { @override ScrollPhysics getScrollPhysics(BuildContext context) => BouncingScrollPhysics(); @override Widget buildOverscrollIndicator(context, child, details) => child; // remove glow }. Apply: MaterialApp(scrollBehavior: MyScrollBehavior()). Per-widget: ScrollConfiguration(behavior: MyScrollBehavior(), child: ListView(...)). BouncingScrollPhysics for iOS bounce, ClampingScrollPhysics for Android clamp. NeverScrollableScrollPhysics to disable scrolling."
        },
        {
            "instruction": "How do you implement pagination with infinite scroll in Flutter?",
            "input": "",
            "output": "ScrollController _controller; @override void initState() { _controller = ScrollController()..addListener(() { if (_controller.position.pixels >= _controller.position.maxScrollExtent - 200 && !_isLoading && _hasMore) { _loadMore(); } }); loadInitial(); }. Track state: bool _isLoading, bool _hasMore, int _page. Build: ListView.builder(controller: _controller, itemCount: items.length + (_hasMore ? 1 : 0), itemBuilder: (ctx, i) { if (i == items.length) return CircularProgressIndicator(); return ItemWidget(items[i]); });. Use infinite_scroll_pagination package for production."
        },
        {
            "instruction": "How do you implement a webview in Flutter?",
            "input": "",
            "output": "Use webview_flutter package. WebViewWidget(controller: WebViewController()..setJavaScriptMode(JavaScriptMode.unrestricted)..setNavigationDelegate(NavigationDelegate(onPageStarted: (url) {}, onPageFinished: (url) {}, onNavigationRequest: (request) { if (request.url.startsWith('https://blocked.com')) return NavigationDecision.prevent; return NavigationDecision.navigate; }))..loadRequest(Uri.parse('https://flutter.dev')));. Run JS: controller.runJavaScript('document.title'). Add channels for JS-Dart communication."
        },
        {
            "instruction": "How do you implement a chat UI in Flutter?",
            "input": "",
            "output": "Chat UI pattern: ListView.builder(reverse: true, controller: _scrollController, itemCount: messages.length, itemBuilder: (context, index) { final msg = messages[index]; return Align(alignment: msg.isMine ? Alignment.centerRight : Alignment.centerLeft, child: Container(margin: EdgeInsets.symmetric(v: 4, h: 8), padding: EdgeInsets.all(12), decoration: BoxDecoration(color: msg.isMine ? Colors.blue : Colors.grey[300], borderRadius: BorderRadius.circular(16)), child: Text(msg.text, style: TextStyle(color: msg.isMine ? Colors.white : Colors.black)))); });. Use reverse: true so new messages appear at bottom. Auto-scroll on send."
        },
        {
            "instruction": "How do you implement skeleton loading screens in Flutter?",
            "input": "",
            "output": "Skeleton loading mimics content layout during loading. Create placeholder widgets matching actual content shape: Container(decoration: BoxDecoration(color: Colors.grey[300], borderRadius: BorderRadius.circular(4))); Animate with ShaderMask and LinearGradient sweep: AnimationController drives gradient position across placeholders. Use skeletonizer package for automatic skeleton generation: Skeletonizer(enabled: isLoading, child: ActualContentWidget()). It automatically creates bone-shaped placeholders matching child widget tree. Better UX than spinners."
        },
        {
            "instruction": "How do you implement gesture-based navigation (swipe to go back)?",
            "input": "",
            "output": "iOS-style swipe back is automatic with CupertinoPageRoute. For custom: use GestureDetector with onHorizontalDragUpdate/End, track drag distance, call Navigator.pop when threshold reached. Or use WillPopScope: WillPopScope(onWillPop: () async { return showConfirmDialog(); }, child: Scaffold(...)). In newer Flutter, use PopScope: PopScope(canPop: false, onPopInvokedWithResult: (didPop, result) { if (!didPop) showConfirmDialog(); }, child: Scaffold(...)). PageView with PageController enables swipe between pages."
        },
        {
            "instruction": "How do you implement a floating action button speed dial in Flutter?",
            "input": "",
            "output": "Custom speed dial: Stack children with AnimatedPositioned FABs. Toggle: FloatingActionButton(onPressed: () => setState(() => _isOpen = !_isOpen)). Sub-buttons: AnimatedOpacity + AnimatedContainer moving vertically. Or use flutter_speed_dial package: SpeedDial(animatedIcon: AnimatedIcons.menu_close, children: [SpeedDialChild(child: Icon(Icons.camera), label: 'Camera', onTap: () {}), SpeedDialChild(child: Icon(Icons.photo), label: 'Gallery', onTap: () {})]);. Overlay with semi-transparent backdrop when open."
        },
        # --- More Intermediate Questions - Batch 2 ---
        # Debugging & DevTools
        {
            "instruction": "How do you use Flutter DevTools for debugging?",
            "input": "",
            "output": "Flutter DevTools is a suite of debugging tools. Launch: flutter run then open DevTools URL, or from IDE. Key panels: 1) Widget Inspector: explore widget tree, view properties, toggle debug paint. 2) Timeline: analyze frame rendering, identify jank. 3) Memory: track allocations, detect leaks, take heap snapshots. 4) Network: monitor HTTP requests/responses. 5) Logging: view print() and log() output. 6) Performance overlay: toggle with WidgetsApp.showPerformanceOverlay. CPU profiler for identifying expensive functions."
        },
        {
            "instruction": "How do you use debug print and logging in Flutter?",
            "input": "",
            "output": "Basic: print('message') or debugPrint('message'). debugPrint throttles output to avoid dropping lines. For structured logging: import 'dart:developer'; log('message', name: 'MyApp', error: exception, stackTrace: stack);. Conditional: assert(() { debugPrint('only in debug'); return true; }());. Check mode: kDebugMode, kProfileMode, kReleaseMode from foundation. Use logger package for levels: Logger().d('debug'), .i('info'), .w('warning'), .e('error'). Remove prints in production."
        },
        {
            "instruction": "How do you inspect the widget tree in Flutter?",
            "input": "",
            "output": "Methods: 1) Flutter Inspector in IDE: view widget hierarchy, select widgets, see properties. 2) DevTools Widget Inspector: interactive tree with details panel. 3) debugDumpApp() prints entire widget tree to console. 4) debugDumpRenderTree() shows render objects. 5) debugDumpLayerTree() shows compositing layers. 6) Add Debug Paint: debugPaintSizeEnabled = true shows layout boundaries. 7) MaterialApp(showSemanticsDebugger: true) shows accessibility tree. 8) Use WidgetInspectorService for programmatic access."
        },
        # Layouts
        {
            "instruction": "How do you implement a grid layout in Flutter?",
            "input": "",
            "output": "GridView options: 1) GridView.count(crossAxisCount: 2, children: [...]) for fixed column count. 2) GridView.builder(gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount: 3, crossAxisSpacing: 10, mainAxisSpacing: 10, childAspectRatio: 1.5), itemCount: 20, itemBuilder: (ctx, i) => Card(...)). 3) SliverGridDelegateWithMaxCrossAxisExtent(maxCrossAxisExtent: 200) for responsive columns. 4) flutter_staggered_grid_view for Pinterest-style masonry layout. Use shrinkWrap: true inside ScrollView."
        },
        {
            "instruction": "How do you create a wrap layout in Flutter?",
            "input": "",
            "output": "Wrap automatically flows children to next line when space runs out. Wrap(spacing: 8, runSpacing: 8, children: tags.map((tag) => Chip(label: Text(tag))).toList());. Properties: direction (horizontal/vertical), alignment (start/center/end/spaceBetween), runAlignment, crossAxisAlignment, spacing (between children), runSpacing (between lines). Unlike Row, Wrap doesn't overflow — it wraps. Useful for tag clouds, filter chips, dynamic button groups."
        },
        {
            "instruction": "How do you use CustomScrollView with Slivers?",
            "input": "",
            "output": "CustomScrollView composes scroll effects with slivers. CustomScrollView(slivers: [SliverAppBar(expandedHeight: 200, floating: true, pinned: true, flexibleSpace: FlexibleSpaceBar(title: Text('Title'), background: Image.network(url, fit: BoxFit.cover))), SliverPadding(padding: EdgeInsets.all(16), sliver: SliverGrid(delegate: SliverChildBuilderDelegate((ctx, i) => Card(), childCount: 10), gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount: 2))), SliverList(delegate: SliverChildListDelegate([...]))]);. Slivers enable complex scrolling with mixed layouts."
        },
        {
            "instruction": "How do you create a table layout in Flutter?",
            "input": "",
            "output": "Table widget: Table(border: TableBorder.all(), columnWidths: {0: FlexColumnWidth(2), 1: FlexColumnWidth(1)}, children: [TableRow(decoration: BoxDecoration(color: Colors.grey[200]), children: [Padding(padding: EdgeInsets.all(8), child: Text('Name', style: TextStyle(fontWeight: FontWeight.bold))), Padding(padding: EdgeInsets.all(8), child: Text('Age'))]), TableRow(children: [Padding(padding: EdgeInsets.all(8), child: Text('John')), Padding(padding: EdgeInsets.all(8), child: Text('25'))])]);. For scrollable data tables: DataTable or PaginatedDataTable with DataColumn and DataRow."
        },
        {
            "instruction": "How do you implement a collapsible/expandable section in Flutter?",
            "input": "",
            "output": "AnimatedContainer: AnimatedContainer(duration: Duration(ms: 300), height: _expanded ? 200 : 0, child: SingleChildScrollView(child: content));. AnimatedCrossFade: AnimatedCrossFade(firstChild: SizedBox.shrink(), secondChild: ExpandedContent(), crossFadeState: _expanded ? CrossFadeState.showSecond : CrossFadeState.showFirst, duration: Duration(ms: 300));. Or use ExpansionTile, ExpansionPanelList. Custom: use SizeTransition with AnimationController for precise control."
        },
        # Streams & Reactive
        {
            "instruction": "How do you use StreamBuilder in Flutter?",
            "input": "",
            "output": "StreamBuilder listens to a Stream and rebuilds on new data. StreamBuilder<int>(stream: counterStream, initialData: 0, builder: (context, snapshot) { if (snapshot.hasError) return Text('Error: ${snapshot.error}'); if (snapshot.connectionState == ConnectionState.waiting) return CircularProgressIndicator(); return Text('Count: ${snapshot.data}'); });. ConnectionState values: none, waiting, active, done. Use with Firebase streams, WebSocket streams, BLoC state streams. Always handle loading, error, and data states."
        },
        {
            "instruction": "How do you create and use Streams in Dart?",
            "input": "",
            "output": "Single-subscription: Stream<int>.periodic(Duration(seconds: 1), (count) => count).take(10);. Broadcast: final controller = StreamController<String>.broadcast(); controller.sink.add('data'); controller.stream.listen((data) => print(data));. Async generator: Stream<int> countStream() async* { for (int i = 0; i < 5; i++) { await Future.delayed(Duration(seconds: 1)); yield i; } }. Transform: stream.map((x) => x * 2).where((x) => x > 5).distinct(). Close controllers in dispose()."
        },
        {
            "instruction": "How do you use StreamController in Flutter?",
            "input": "",
            "output": "StreamController creates a stream you can add data to. final _controller = StreamController<String>();. Add data: _controller.sink.add('Hello');. Add error: _controller.sink.addError('Oops');. Listen: _controller.stream.listen((data) {}, onError: (err) {}, onDone: () {});. For multiple listeners: StreamController<String>.broadcast(). Transform: _controller.stream.transform(StreamTransformer.fromHandlers(handleData: (data, sink) { sink.add(data.toUpperCase()); }));. Always close: _controller.close() in dispose()."
        },
        # Widgets Deep Dive
        {
            "instruction": "How do you implement a custom AppBar in Flutter?",
            "input": "",
            "output": "PreferredSize widget: AppBar(toolbarHeight: 80, flexibleSpace: Container(decoration: BoxDecoration(gradient: LinearGradient(colors: [Colors.blue, Colors.purple]))), title: Text('Custom'), actions: [IconButton(icon: Badge(label: Text('3'), child: Icon(Icons.notifications)), onPressed: () {})]);. Fully custom: PreferredSize(preferredSize: Size.fromHeight(100), child: Container(padding: EdgeInsets.only(top: MediaQuery.of(context).padding.top), child: Row(...)));. Or use SliverAppBar for scroll-collapsing behavior."
        },
        {
            "instruction": "How do you use ClipRRect and ClipPath in Flutter?",
            "input": "",
            "output": "ClipRRect rounds corners: ClipRRect(borderRadius: BorderRadius.circular(20), child: Image.network(url, fit: BoxFit.cover));. ClipOval for circles: ClipOval(child: Image.asset('avatar.png', width: 100, height: 100, fit: BoxFit.cover));. ClipPath for custom shapes: ClipPath(clipper: MyClipper(), child: Container(color: Colors.blue)); class MyClipper extends CustomClipper<Path> { @override Path getClip(Size size) { var path = Path()..lineTo(0, size.height - 50)..quadraticBezierTo(size.width/2, size.height, size.width, size.height - 50)..lineTo(size.width, 0)..close(); return path; } }."
        },
        {
            "instruction": "How do you implement a PageView with indicators in Flutter?",
            "input": "",
            "output": "PageView with dot indicators: int _currentPage = 0; PageView(controller: _pageController, onPageChanged: (i) => setState(() => _currentPage = i), children: pages);. Dots: Row(mainAxisAlignment: MainAxisAlignment.center, children: List.generate(pages.length, (i) => Container(margin: EdgeInsets.all(4), width: _currentPage == i ? 12 : 8, height: 8, decoration: BoxDecoration(color: _currentPage == i ? Colors.blue : Colors.grey, borderRadius: BorderRadius.circular(4)))));. Use smooth_page_indicator for animated indicators. TabPageSelector for Material-style dots."
        },
        {
            "instruction": "How do you implement a BottomSheet with a handle in Flutter?",
            "input": "",
            "output": "showModalBottomSheet(context: context, isScrollControlled: true, shape: RoundedRectangleBorder(borderRadius: BorderRadius.vertical(top: Radius.circular(20))), builder: (context) => DraggableScrollableSheet(initialChildSize: 0.5, minChildSize: 0.25, maxChildSize: 0.9, expand: false, builder: (context, scrollController) => Column(children: [Container(width: 40, height: 4, margin: EdgeInsets.symmetric(vertical: 12), decoration: BoxDecoration(color: Colors.grey[400], borderRadius: BorderRadius.circular(2))), Expanded(child: ListView.builder(controller: scrollController, itemCount: 50, itemBuilder: (ctx, i) => ListTile(title: Text('Item $i'))))])));."
        },
        {
            "instruction": "How do you use the Visibility widget in Flutter?",
            "input": "",
            "output": "Visibility(visible: _showWidget, child: Text('Hello'));. When visible=false, the child is hidden but can still take space. Properties: maintainState (keep state alive), maintainAnimation, maintainSize (keep size), maintainInteractivity. Visibility(visible: false, maintainSize: true, maintainAnimation: true, maintainState: true, child: button) — invisible but occupies space. Alternative: if (_show) Widget() for conditional rendering (destroys widget). Offstage(offstage: true, child: ...) hides but keeps state."
        },
        {
            "instruction": "How do you use the FittedBox widget?",
            "input": "",
            "output": "FittedBox scales and positions its child within itself. FittedBox(fit: BoxFit.contain, child: Text('Long text that should scale down'));. BoxFit options: contain (scale to fit), cover (scale to fill), fill (stretch), fitWidth, fitHeight, scaleDown (only shrink, never enlarge), none. Useful for: auto-scaling text to container width, fitting images, preventing text overflow. Combine with constraints: SizedBox(width: 200, child: FittedBox(child: Text('Scaled')))."
        },
        {
            "instruction": "How do you implement a badge/notification counter in Flutter?",
            "input": "",
            "output": "Material 3 Badge: Badge(label: Text('5'), child: Icon(Icons.notifications));. Badge without label (dot): Badge(child: Icon(Icons.mail));. Custom badge: Stack(children: [Icon(Icons.shopping_cart, size: 30), Positioned(right: 0, top: 0, child: Container(padding: EdgeInsets.all(2), decoration: BoxDecoration(color: Colors.red, borderRadius: BorderRadius.circular(10)), constraints: BoxConstraints(minWidth: 16, minHeight: 16), child: Text('3', style: TextStyle(color: Colors.white, fontSize: 10), textAlign: TextAlign.center)))]);. Use badge with BottomNavigationBarItem."
        },
        # State Management Patterns
        {
            "instruction": "How do you implement the Repository pattern in Flutter?",
            "input": "",
            "output": "Repository abstracts data sources. 1) Define interface: abstract class UserRepository { Future<List<User>> getUsers(); Future<User> getUserById(int id); }. 2) Implement: class UserRepositoryImpl implements UserRepository { final ApiService _api; final LocalDb _db; Future<List<User>> getUsers() async { try { final users = await _api.fetchUsers(); await _db.cacheUsers(users); return users; } catch (_) { return _db.getCachedUsers(); } } }. 3) Inject: Provider<UserRepository>(create: (_) => UserRepositoryImpl(api, db)). Enables testing with mock repositories."
        },
        {
            "instruction": "How do you implement the singleton pattern in Dart?",
            "input": "",
            "output": "Factory constructor singleton: class Database { static final Database _instance = Database._internal(); factory Database() => _instance; Database._internal(); Future<void> connect() async { } }. Usage: final db = Database(); // always same instance. Alternative with late initialization: class ApiClient { static ApiClient? _instance; static ApiClient get instance { _instance ??= ApiClient._(); return _instance!; } ApiClient._(); }. Singletons are useful for services but can make testing harder — prefer dependency injection."
        },
        {
            "instruction": "How do you debounce search input in Flutter?",
            "input": "",
            "output": "Debouncing delays action until user stops typing. Timer? _debounce; void _onSearchChanged(String query) { if (_debounce?.isActive ?? false) _debounce!.cancel(); _debounce = Timer(Duration(milliseconds: 500), () { performSearch(query); }); }. TextFormField(onChanged: _onSearchChanged);. Dispose: _debounce?.cancel() in dispose(). With RxDart: _searchSubject.debounceTime(Duration(milliseconds: 500)).distinct().switchMap((query) => searchApi(query)).listen((results) => setState(() => _results = results)). Prevents excessive API calls."
        },
        {
            "instruction": "How do you implement event bus pattern in Flutter?",
            "input": "",
            "output": "Event bus enables loose coupling between components. Using StreamController: class EventBus { static final EventBus _instance = EventBus._(); factory EventBus() => _instance; EventBus._(); final _controller = StreamController.broadcast(); Stream<T> on<T>() => _controller.stream.where((e) => e is T).cast<T>(); void fire(event) => _controller.add(event); void dispose() => _controller.close(); }. Fire: EventBus().fire(UserLoggedIn(user)). Listen: EventBus().on<UserLoggedIn>().listen((e) => updateUI(e.user)). Alternative: use event_bus package."
        },
        # Flutter Web & Desktop
        {
            "instruction": "How do you handle platform-specific code in Flutter?",
            "input": "",
            "output": "Check platform: import 'dart:io'; if (Platform.isAndroid) { } else if (Platform.isIOS) { }. For web: import 'package:flutter/foundation.dart'; if (kIsWeb) { }. Conditional imports: import 'stub.dart' if (dart.library.html) 'web_impl.dart' if (dart.library.io) 'mobile_impl.dart';. Use defaultTargetPlatform for UI decisions. Platform channels for native code: MethodChannel('com.app/native').invokeMethod('getNativeData'). Abstract platform differences behind interfaces."
        },
        {
            "instruction": "How do you optimize Flutter web performance?",
            "input": "",
            "output": "1) Use CanvasKit renderer for rich graphics: flutter build web --web-renderer canvaskit. 2) Use HTML renderer for smaller download: --web-renderer html. 3) Enable deferred loading: import 'heavy_page.dart' deferred as heavy; await heavy.loadLibrary();. 4) Optimize images: use WebP format, lazy load. 5) Tree shake icons: --tree-shake-icons. 6) Minimize package usage. 7) Use --release flag. 8) Configure service worker caching. 9) Avoid excessive widget rebuilds. 10) Use flutter build web --pwa-strategy=offline-first for PWA."
        },
        {
            "instruction": "How do you implement responsive web layout in Flutter?",
            "input": "",
            "output": "Use LayoutBuilder for breakpoints: LayoutBuilder(builder: (ctx, constraints) { if (constraints.maxWidth > 1200) return DesktopLayout(); if (constraints.maxWidth > 600) return TabletLayout(); return MobileLayout(); });. Navigation: mobile=BottomNavigationBar, tablet=NavigationRail, desktop=full Sidebar. Use Flexible/Expanded for fluid widths. ConstrainedBox(constraints: BoxConstraints(maxWidth: 1200)) for max content width. MediaQuery.of(context).size for screen dimensions. responsive_framework package automates breakpoint handling."
        },
        # Accessibility
        {
            "instruction": "How do you implement accessibility in Flutter?",
            "input": "",
            "output": "1) Semantics: Semantics(label: 'Close button', button: true, child: GestureDetector(...)). 2) ExcludeSemantics: hides decorative elements from screen readers. 3) MergeSemantics: combines child semantics. 4) Sufficient contrast: follow WCAG guidelines. 5) Large touch targets: minimum 48x48 dp. 6) Text scaling: respect MediaQuery.textScaleFactor. 7) Focus management: FocusNode, autofocus. 8) Test with: MaterialApp(showSemanticsDebugger: true). 9) Image.asset(semanticLabel: 'Logo'). 10) Use Tooltip for icon buttons."
        },
        # State Persistence
        {
            "instruction": "How do you implement state restoration in Flutter?",
            "input": "",
            "output": "RestorationMixin preserves state across app restarts. class MyPageState extends State<MyPage> with RestorationMixin { final RestorableInt _counter = RestorableInt(0); @override String get restorationId => 'my_page'; @override void restoreState(RestorationBucket? old, bool initial) { registerForRestoration(_counter, 'counter'); } void increment() => setState(() => _counter.value++); @override void dispose() { _counter.dispose(); super.dispose(); } }. Enable: MaterialApp(restorationScopeId: 'app'). Works for scroll position, form input, navigation state."
        },
        {
            "instruction": "How do you implement offline-first architecture in Flutter?",
            "input": "",
            "output": "Offline-first pattern: 1) Always read from local cache first. 2) Sync with server when online. 3) Queue mutations offline, replay when connected. Implementation: class OfflineFirstRepo { Future<List<Item>> getItems() async { final cached = await localDb.getItems(); refreshInBackground(); return cached; } Future<void> refreshInBackground() async { if (await isOnline()) { final remote = await api.fetchItems(); await localDb.saveItems(remote); notifyListeners(); } } }. Use connectivity_plus to detect network. Hive or Drift for local storage. Show sync status indicator."
        },
        # Advanced Widgets
        {
            "instruction": "How do you use the Overlay widget in Flutter?",
            "input": "",
            "output": "Overlay displays floating widgets above others. OverlayEntry entry = OverlayEntry(builder: (context) => Positioned(top: 100, left: 50, child: Material(elevation: 8, child: Container(padding: EdgeInsets.all(16), child: Text('Overlay content')))));. Show: Overlay.of(context).insert(entry);. Remove: entry.remove();. Mark rebuild: entry.markNeedsBuild();. Use for custom tooltips, dropdown menus, floating tutorials. CompositedTransformTarget + CompositedTransformFollower for positioning relative to a widget."
        },
        {
            "instruction": "How do you implement a carousel/slider in Flutter?",
            "input": "",
            "output": "Using PageView: PageView.builder(controller: PageController(viewportFraction: 0.85), itemCount: items.length, itemBuilder: (ctx, i) => AnimatedContainer(duration: Duration(ms: 300), margin: EdgeInsets.symmetric(h: 10, v: _currentPage == i ? 0 : 20), decoration: BoxDecoration(borderRadius: BorderRadius.circular(16), image: DecorationImage(image: NetworkImage(items[i].url), fit: BoxFit.cover))));. Auto-scroll: Timer.periodic(Duration(seconds: 3), (_) => _controller.nextPage(...)). Use carousel_slider package for ready-made carousel with indicators."
        },
        {
            "instruction": "How do you implement a color picker in Flutter?",
            "input": "",
            "output": "Use flutter_colorpicker package. Color _color = Colors.blue; showDialog(context: context, builder: (_) => AlertDialog(title: Text('Pick color'), content: SingleChildScrollView(child: ColorPicker(pickerColor: _color, onColorChanged: (color) => _color = color, enableAlpha: true, displayThumbColor: true)), actions: [TextButton(onPressed: () => Navigator.pop(context), child: Text('Done'))]));. Types: BlockPicker (simple grid), MaterialPicker (Material swatches), ColorPicker (HSV/HSL wheel). Store as int: color.value."
        },
        {
            "instruction": "How do you implement animated bottom navigation in Flutter?",
            "input": "",
            "output": "Custom animated nav: BottomNavigationBar with custom selected/unselected styling. Or build custom: Container(child: Row(mainAxisAlignment: MainAxisAlignment.spaceAround, children: items.map((item) => GestureDetector(onTap: () => setState(() => _selected = item.index), child: AnimatedContainer(duration: Duration(ms: 200), padding: EdgeInsets.symmetric(h: 16, v: 8), decoration: BoxDecoration(color: _selected == item.index ? Colors.blue.withOpacity(0.1) : Colors.transparent, borderRadius: BorderRadius.circular(20)), child: Row(children: [Icon(item.icon, color: _selected == item.index ? Colors.blue : Colors.grey), if (_selected == item.index) Text(item.label)]))))));."
        },
        {
            "instruction": "How do you implement a range slider in Flutter?",
            "input": "",
            "output": "RangeSlider(values: _rangeValues, min: 0, max: 100, divisions: 20, labels: RangeLabels('${_rangeValues.start.round()}', '${_rangeValues.end.round()}'), onChanged: (values) => setState(() => _rangeValues = values));. Customize with SliderTheme: SliderTheme(data: SliderThemeData(activeTrackColor: Colors.blue, inactiveTrackColor: Colors.blue[100], thumbColor: Colors.blue, overlayColor: Colors.blue.withOpacity(0.2), rangeThumbShape: RoundRangeSliderThumbShape(enabledThumbRadius: 12)), child: RangeSlider(...)). Useful for price filters."
        },
        # Dependencies & Build
        {
            "instruction": "How do you use build_runner for code generation in Flutter?",
            "input": "",
            "output": "build_runner generates code from annotations. Setup: add build_runner and generators (json_serializable, freezed, mockito) to dev_dependencies. Annotate: @JsonSerializable() class User { final String name; User(this.name); factory User.fromJson(Map<String, dynamic> json) => _$UserFromJson(json); Map<String, dynamic> toJson() => _$UserToJson(this); }. Generate: dart run build_runner build. Watch: dart run build_runner watch. Clean: dart run build_runner clean. Generated files end in .g.dart or .freezed.dart. Add to .gitignore or commit — team preference."
        },
        {
            "instruction": "How do you implement flavor/environment builds in Flutter?",
            "input": "",
            "output": "Flavors create distinct app configurations. Android: productFlavors { dev { applicationIdSuffix '.dev'; resValue 'string', 'app_name', 'MyApp Dev' } prod { resValue 'string', 'app_name', 'MyApp' } }. iOS: create schemes and configurations in Xcode. Run: flutter run --flavor dev -t lib/main_dev.dart. Entry points per flavor: main_dev.dart, main_prod.dart. Set config: class FlavorConfig { final String apiUrl; static late FlavorConfig instance; FlavorConfig({required this.apiUrl}); }. Use --dart-define for simpler env vars without full flavors."
        },
        # Dart Language
        {
            "instruction": "How do you use extension methods in Dart?",
            "input": "",
            "output": "Extensions add methods to existing types. extension StringExtension on String { String capitalize() => '${this[0].toUpperCase()}${substring(1)}'; bool get isEmail => RegExp(r'^[\\w-\\.]+@[\\w-]+\\.[a-z]+$').hasMatch(this); String truncate(int maxLen) => length <= maxLen ? this : '${substring(0, maxLen)}...'; }. Usage: 'hello'.capitalize(); // Hello. 'test@email.com'.isEmail; // true. Extension on nullable: extension on int? { int orZero() => this ?? 0; }. Named extensions can be imported selectively."
        },
        {
            "instruction": "How do you use mixins in Dart?",
            "input": "",
            "output": "Mixins add functionality to classes without inheritance. mixin Loggable { void log(String message) => print('[${runtimeType}] $message'); } mixin Serializable { Map<String, dynamic> toMap(); String toJsonString() => jsonEncode(toMap()); }. Use: class User with Loggable, Serializable { final String name; User(this.name); @override Map<String, dynamic> toMap() => {'name': name}; }. Restrict with on: mixin ValidatorMixin on StatefulWidget { }. Dart 3 mixin class combines class and mixin. Mixins cannot have constructors."
        },
        {
            "instruction": "How do you use generics in Dart?",
            "input": "",
            "output": "Generics enable type-safe reusable code. Class: class Box<T> { final T value; Box(this.value); T get() => value; }. Bounded: class NumberBox<T extends num> { T add(T a, T b); }. Function: T first<T>(List<T> items) => items[0];. Multiple types: class Pair<A, B> { final A first; final B second; Pair(this.first, this.second); }. Use: var box = Box<String>('hello'); var pair = Pair<String, int>('age', 25);. Dart infers types when possible. Common in collections, futures, streams."
        },
        {
            "instruction": "How do you use records and pattern matching in Dart 3?",
            "input": "",
            "output": "Records are anonymous immutable aggregates. Named: ({String name, int age}) person = (name: 'John', age: 25); print(person.name);. Positional: (String, int) pair = ('hello', 42); print(pair.$1);. Pattern matching: switch (shape) { case Circle(radius: var r) => pi * r * r, case Rectangle(w: var w, h: var h) => w * h }. Destructuring: var (name, age) = getUserData();. if-case: if (json case {'name': String name}) { use(name); }. Guard: case Circle(r: var r) when r > 0 =>."
        },
        {
            "instruction": "How do you handle null safety in Dart?",
            "input": "",
            "output": "Dart's sound null safety: types non-nullable by default. Nullable: String? name;. Null-aware operators: name?.length (null-safe access), name ?? 'default' (null coalescing), name ??= 'value' (null-aware assignment), list?[0] (null-aware index). Late: late String name; (initialized before use, no null check). Required named: void fn({required String name}) {}. Bang operator: name! (assert non-null, throws if null). Type promotion: if (name != null) { name.length; // promoted to String }."
        },
        {
            "instruction": "How do you implement the factory pattern in Dart?",
            "input": "",
            "output": "Factory constructors return instances without always creating new ones. abstract class Shape { double area(); factory Shape.circle(double radius) => Circle(radius); factory Shape.square(double side) => Square(side); factory Shape.fromJson(Map<String, dynamic> json) { switch (json['type']) { case 'circle': return Circle(json['radius']); case 'square': return Square(json['side']); default: throw ArgumentError('Unknown shape'); } } } class Circle implements Shape { final double radius; Circle(this.radius); double area() => 3.14 * radius * radius; }. Factories enable polymorphic construction."
        },
        # Error handling & Async
        {
            "instruction": "How do you use Isolates in Flutter?",
            "input": "",
            "output": "Isolates run code on separate threads. Simple: final result = await compute(expensiveFunction, data);. compute() runs a function in an isolate and returns the result. For ongoing communication: final receivePort = ReceivePort(); await Isolate.spawn((sendPort) { sendPort.send(heavyComputation()); }, receivePort.sendPort); final result = await receivePort.first;. Use for: JSON parsing, image processing, crypto, heavy math. Dart 2.19+: Isolate.run(() => heavyWork()). Can't access UI or plugins from isolates."
        },
        {
            "instruction": "How do you use the FutureBuilder widget?",
            "input": "",
            "output": "FutureBuilder rebuilds when a Future completes. FutureBuilder<String>(future: fetchData(), builder: (context, snapshot) { if (snapshot.connectionState == ConnectionState.waiting) return CircularProgressIndicator(); if (snapshot.hasError) return Text('Error: ${snapshot.error}'); return Text(snapshot.data!); });. Important: don't create the Future inside build() — store it in initState or a variable, otherwise it refetches on every rebuild. snapshot.connectionState: none, waiting, active, done. snapshot.hasData checks for non-null data."
        },
        {
            "instruction": "How do you handle multiple async operations in Dart?",
            "input": "",
            "output": "Parallel: final results = await Future.wait([fetchUsers(), fetchPosts(), fetchComments()]); — runs all concurrently, completes when all done. Sequential: final user = await fetchUser(); final posts = await fetchPosts(user.id);. First to complete: final result = await Future.any([source1(), source2()]);. With timeout: await fetchData().timeout(Duration(seconds: 5), onTimeout: () => fallbackData);. Error handling: Future.wait has eagerError parameter. Use try/catch for individual handling."
        },
        # Navigation Extras
        {
            "instruction": "How do you implement named routes in Flutter?",
            "input": "",
            "output": "Define routes: MaterialApp(initialRoute: '/', routes: {'/': (context) => HomeScreen(), '/details': (context) => DetailsScreen(), '/settings': (context) => SettingsScreen()});. Navigate: Navigator.pushNamed(context, '/details');. With arguments: Navigator.pushNamed(context, '/details', arguments: {'id': 42}); retrieve: ModalRoute.of(context)!.settings.arguments as Map. onGenerateRoute handles dynamic routes: onGenerateRoute: (settings) { if (settings.name == '/user') return MaterialPageRoute(builder: (_) => UserScreen(settings.arguments)); }."
        },
        {
            "instruction": "How do you implement breadcrumb navigation in Flutter?",
            "input": "",
            "output": "Custom breadcrumb: Row(children: breadcrumbs.asMap().entries.map((entry) { final isLast = entry.key == breadcrumbs.length - 1; return Row(children: [InkWell(onTap: isLast ? null : () => navigateTo(entry.value.route), child: Text(entry.value.label, style: TextStyle(color: isLast ? Colors.black : Colors.blue, fontWeight: isLast ? FontWeight.bold : FontWeight.normal))), if (!isLast) Padding(padding: EdgeInsets.symmetric(horizontal: 8), child: Icon(Icons.chevron_right, size: 16))]); }).toList());. Track breadcrumbs in navigation observer or state."
        },
        # Security
        {
            "instruction": "How do you implement API key security in Flutter?",
            "input": "",
            "output": "Never hardcode API keys in source code. Approaches: 1) --dart-define: flutter run --dart-define=API_KEY=xxx; access: const key = String.fromEnvironment('API_KEY');. 2) .env file with flutter_dotenv: await dotenv.load(); dotenv.env['API_KEY'];. 3) Backend proxy: route requests through your server that holds the key. 4) Native storage: store in AndroidManifest/Info.plist, read via MethodChannel. 5) CI/CD: inject secrets during build. 6) For Firebase: google-services.json/GoogleService-Info.plist are safe to commit. Always add .env to .gitignore."
        },
        {
            "instruction": "How do you obfuscate Flutter code?",
            "input": "",
            "output": "Build with obfuscation: flutter build apk --obfuscate --split-debug-info=build/symbols. This renames classes, methods, and variables to meaningless names. --split-debug-info saves symbol map for crash report deobfuscation. For iOS: flutter build ios --obfuscate --split-debug-info=build/symbols. Deobfuscate stack traces: flutter symbolize -i crash.txt -d build/symbols/. ProGuard/R8 additionally obfuscates Java/Kotlin code on Android. Does not protect string literals — use encryption for sensitive strings."
        },
        # Packages & Plugins
        {
            "instruction": "How do you create a custom Flutter package?",
            "input": "",
            "output": "Create: flutter create --template=package my_package. Structure: lib/my_package.dart (barrel file), lib/src/ (implementation), test/ (tests), pubspec.yaml, README.md, CHANGELOG.md, LICENSE. Export public API from barrel: export 'src/my_widget.dart';. For plugins with native code: flutter create --template=plugin --platforms=android,ios my_plugin. Publish: dart pub publish --dry-run then dart pub publish. Use dart pub lints for scoring. Follow package conventions: meaningful CHANGELOG, example/ folder."
        },
        {
            "instruction": "How do you implement dependency injection in Flutter?",
            "input": "",
            "output": "DI approaches: 1) Provider: MultiProvider(providers: [Provider<ApiService>(create: (_) => ApiServiceImpl()), ProxyProvider<ApiService, UserRepo>(update: (_, api, __) => UserRepoImpl(api))], child: App()). 2) get_it service locator: GetIt.I.registerSingleton<ApiService>(ApiServiceImpl()); final api = GetIt.I<ApiService>();. 3) injectable + get_it for code generation: @injectable class UserRepo { final ApiService api; UserRepo(this.api); }. DI enables testability by swapping implementations."
        },
        {
            "instruction": "How do you implement caching strategies with Dio interceptors?",
            "input": "",
            "output": "Custom Dio cache interceptor: class CacheInterceptor extends Interceptor { final Map<String, Response> _cache = {}; @override void onRequest(options, handler) { final cached = _cache[options.uri.toString()]; if (cached != null) { return handler.resolve(cached); } handler.next(options); } @override void onResponse(response, handler) { _cache[response.requestOptions.uri.toString()] = response; handler.next(response); } }. dio.interceptors.add(CacheInterceptor());. For production: use dio_cache_interceptor with file/memory/hive backend. Add TTL, max-age, ETag support."
        },
        {
            "instruction": "How do you implement a custom lint rule in Flutter?",
            "input": "",
            "output": "Configure in analysis_options.yaml: include: package:flutter_lints/flutter.yaml (or lints/recommended.yaml). Override rules: linter: rules: prefer_const_constructors: true, avoid_print: true, always_declare_return_types: true. Custom rules with custom_lint package: create analyzer plugin. Severity levels: info, warning, error. Ignore per-line: // ignore: rule_name. Ignore per-file: // ignore_for_file: rule_name. Popular rulesets: flutter_lints, very_good_analysis, lint."
        },
        {
            "instruction": "How do you optimize images and assets in Flutter?",
            "input": "",
            "output": "1) Resolution-aware images: assets/images/2.0x/logo.png, 3.0x/logo.png — Flutter auto-selects. 2) Compress images before adding: use WebP format for smaller size. 3) Lazy load network images: CachedNetworkImage(imageUrl: url, placeholder: (ctx, url) => CircularProgressIndicator()). 4) Use precacheImage(AssetImage('logo.png'), context) for ahead-of-time loading. 5) AssetBundle for deferred loading. 6) Remove unused assets. 7) SVG for icons/logos — size-independent. 8) flutter build --tree-shake-icons removes unused Material icons."
        },
        # --- Final Intermediate Additions ---
        {
            "instruction": "How do you handle JSON serialization in Flutter?",
            "input": "",
            "output": "Manual: class User { final String name; final int age; User(this.name, this.age); factory User.fromJson(Map<String, dynamic> json) => User(json['name'], json['age']); Map<String, dynamic> toJson() => {'name': name, 'age': age}; }. Decode: final user = User.fromJson(jsonDecode(jsonString));. Encode: String json = jsonEncode(user.toJson());. For code generation: use json_serializable with @JsonSerializable() annotation. Run dart run build_runner build. Handles nested objects, default values, rename fields with @JsonKey."
        },
        {
            "instruction": "How do you implement state management with ChangeNotifier?",
            "input": "",
            "output": "ChangeNotifier is the simplest state management. class CartModel extends ChangeNotifier { final List<Item> _items = []; List<Item> get items => UnmodifiableListView(_items); double get totalPrice => _items.fold(0, (sum, item) => sum + item.price); void add(Item item) { _items.add(item); notifyListeners(); } void remove(Item item) { _items.remove(item); notifyListeners(); } }. Provide: ChangeNotifierProvider(create: (_) => CartModel(), child: App()). Consume: Consumer<CartModel>(builder: (ctx, cart, child) => Text('Total: ${cart.totalPrice}'))." 
        },
        {
            "instruction": "How do you implement swipe-to-dismiss in Flutter?",
            "input": "",
            "output": "Use Dismissible widget: Dismissible(key: Key(item.id), direction: DismissDirection.endToStart, onDismissed: (direction) { removeItem(item); ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Deleted'))); }, confirmDismiss: (direction) async => await showConfirmDialog(), background: Container(color: Colors.red, alignment: Alignment.centerRight, padding: EdgeInsets.only(right: 20), child: Icon(Icons.delete, color: Colors.white)), child: ListTile(title: Text(item.name)));. Use confirmDismiss for undo patterns."
        },
        {
            "instruction": "How do you implement a splash/onboarding page flow in Flutter?",
            "input": "",
            "output": "Onboarding with PageView: PageView(controller: _controller, children: [OnboardingPage(title: 'Welcome', image: 'assets/1.png'), OnboardingPage(title: 'Features', image: 'assets/2.png'), OnboardingPage(title: 'Get Started', image: 'assets/3.png')]);. Track completion in SharedPreferences: prefs.setBool('onboarded', true);. Main check: final onboarded = prefs.getBool('onboarded') ?? false; return onboarded ? HomeScreen() : OnboardingScreen();. Add dot indicators and skip/next buttons."
        },
        {
            "instruction": "How do you implement aspect-ratio-aware image loading?",
            "input": "",
            "output": "Loading images with correct aspect ratio: Image.network(url, loadingBuilder: (context, child, progress) { if (progress == null) return child; return Center(child: CircularProgressIndicator(value: progress.expectedTotalBytes != null ? progress.cumulativeBytesLoaded / progress.expectedTotalBytes! : null)); }, errorBuilder: (context, error, stackTrace) => Icon(Icons.error));. Use FadeInImage for smooth placeholder transition: FadeInImage.assetNetwork(placeholder: 'assets/placeholder.png', image: url, fit: BoxFit.cover)."
        },
        {
            "instruction": "How do you implement global app state management?",
            "input": "",
            "output": "Global state options: 1) InheritedWidget at root for simple cases. 2) Provider at MaterialApp level: MultiProvider(providers: [ChangeNotifierProvider(create: (_) => AuthState()), ChangeNotifierProvider(create: (_) => ThemeState())], child: MaterialApp(...)). 3) GetIt service locator: register services as singletons, access anywhere. 4) Riverpod ProviderScope wrapping entire app. 5) Global ValueNotifier for simple values. Choose based on complexity: simple → Provider, medium → Riverpod, complex → Bloc."
        },
        {
            "instruction": "How do you implement a settings page in Flutter?",
            "input": "",
            "output": "Settings page with SwitchListTile and ListTile: ListView(children: [SwitchListTile(title: Text('Dark Mode'), subtitle: Text('Enable dark theme'), value: _isDark, onChanged: (val) => setState(() => _isDark = val)), ListTile(title: Text('Language'), subtitle: Text('English'), trailing: Icon(Icons.chevron_right), onTap: () => showLanguagePicker()), ListTile(title: Text('Clear Cache'), onTap: () async { await clearCache(); showSnackBar('Cache cleared'); })]);. Persist with SharedPreferences. Group sections with header ListTiles."
        },
        {
            "instruction": "How do you implement scroll-to-top functionality in Flutter?",
            "input": "",
            "output": "Use ScrollController: final _scrollController = ScrollController();. Scroll to top: _scrollController.animateTo(0, duration: Duration(milliseconds: 500), curve: Curves.easeOut);. Show FAB when scrolled: _scrollController.addListener(() { setState(() => _showScrollToTop = _scrollController.offset > 200); });. FloatingActionButton(onPressed: () => _scrollController.animateTo(0, ...), child: Icon(Icons.arrow_upward), mini: true). Dispose controller in dispose()."
        },
        {
            "instruction": "How do you handle app lifecycle events in Flutter?",
            "input": "",
            "output": "Use WidgetsBindingObserver: class _MyState extends State<MyPage> with WidgetsBindingObserver { @override void initState() { super.initState(); WidgetsBinding.instance.addObserver(this); } @override void didChangeAppLifecycleState(AppLifecycleState state) { switch (state) { case AppLifecycleState.resumed: refreshData(); break; case AppLifecycleState.paused: saveState(); break; case AppLifecycleState.inactive: pauseVideo(); break; case AppLifecycleState.detached: cleanup(); break; } } @override void dispose() { WidgetsBinding.instance.removeObserver(this); super.dispose(); } }."
        },
        {
            "instruction": "How do you implement copy-to-clipboard with toast feedback?",
            "input": "",
            "output": "Copy and notify: GestureDetector(onLongPress: () async { await Clipboard.setData(ClipboardData(text: textToCopy)); ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Copied to clipboard'), duration: Duration(seconds: 2), behavior: SnackBarBehavior.floating)); }, child: SelectableText(textToCopy));. For SelectableText: SelectableText(data, onTap: () { Clipboard.setData(ClipboardData(text: data)); }). Use fluttertoast package for toast-style notifications instead of SnackBar."
        },
    ]


def generate_advanced_questions():
    """Generate advanced-level Flutter Q&A pairs."""
    return [
        # State Management Deep Dives
        {
            "instruction": "How does the Bloc library handle state management in Flutter?",
            "input": "",
            "output": "The Bloc library implements unidirectional data flow: UI dispatches Events to a Bloc, which processes them through on<Event> handlers and emits new States. BlocProvider supplies the Bloc via InheritedWidget, BlocBuilder rebuilds UI on state changes, BlocListener handles side effects, and BlocConsumer combines both. The pattern ensures testable, predictable state transitions with full event traceability."
        },
        {
            "instruction": "How does Provider work internally in Flutter?",
            "input": "",
            "output": "Provider is built on top of InheritedWidget. ChangeNotifierProvider creates a ChangeNotifier and exposes it via an InheritedProvider higher in the widget tree. When notifyListeners() is called, the InheritedWidget marks dependent elements as dirty, triggering rebuilds. context.watch() subscribes to changes via InheritedWidget.dependOnInheritedElement, while context.read() accesses without subscribing."
        },
        {
            "instruction": "What are the advantages of Riverpod over Provider?",
            "input": "",
            "output": "Riverpod improves on Provider in several ways: it doesn't depend on BuildContext (providers are global), catches provider errors at compile time instead of runtime, supports multiple providers of the same type, enables provider overriding for testing, supports auto-disposal of unused providers, and provides family modifiers for parameterized providers. It also avoids the ProviderNotFoundException."
        },
        {
            "instruction": "What is the Redux pattern and how is it used in Flutter?",
            "input": "",
            "output": "Redux is a state management pattern with a single immutable Store, Actions that describe state changes, and Reducers (pure functions) that create new state from old state plus an action. In Flutter, flutter_redux provides StoreProvider to supply the Store and StoreConnector to rebuild widgets on state changes. Middleware handles async operations like API calls."
        },
        {
            "instruction": "How do you implement a singleton pattern in Dart?",
            "input": "",
            "output": "In Dart, a singleton is implemented using a factory constructor and a static private instance: class MyClass { static final MyClass _instance = MyClass._internal(); factory MyClass() => _instance; MyClass._internal(); }. The factory constructor always returns the same instance. Dart's static final ensures lazy initialization and thread safety."
        },
        # Performance Optimization
        {
            "instruction": "How do you optimize Flutter app performance?",
            "input": "",
            "output": "Key Flutter performance optimizations include: using const constructors to avoid unnecessary rebuilds, minimizing widget tree depth, using ListView.builder for lazy rendering, avoiding expensive operations in build(), wrapping animated widgets in RepaintBoundary, using Isolates for heavy computation, caching images, reducing shader compilations with warm-up, and profiling with Flutter DevTools."
        },
        {
            "instruction": "What are Isolates in Flutter and when should you use them?",
            "input": "",
            "output": "Isolates are independent execution threads in Dart that don't share memory, communicating via message passing. Unlike threads, isolates have their own memory heap, preventing data races. Use compute() for simple one-shot heavy computations (JSON parsing, image processing) or spawn Isolates for continuous background work. They prevent UI jank from expensive operations on the main isolate."
        },
        {
            "instruction": "What is the compute() function in Flutter?",
            "input": "",
            "output": "compute() is a convenience function that runs a function on a separate Isolate and returns the result. It handles Isolate creation and message passing. It takes a top-level function and an argument, executes the function on a background Isolate, and returns the result as a Future. It is useful for expensive operations like JSON parsing large responses."
        },
        {
            "instruction": "What is tree shaking in Flutter?",
            "input": "",
            "output": "Tree shaking is a compiler optimization that removes unused code from the final build. During release mode compilation, the Dart compiler analyzes which classes, functions, and methods are actually referenced and excludes everything else. This reduces app size by eliminating dead code. It works with AOT compilation and is automatic in Flutter release builds."
        },
        {
            "instruction": "How do you reduce Flutter app size?",
            "input": "",
            "output": "Reduce Flutter app size by: using --split-debug-info to extract debug symbols, enabling code obfuscation with --obfuscate, using app bundles instead of APKs for Android, removing unused packages and assets, compressing images, using deferred loading for rarely used features, enabling R8/ProGuard for Android, and running flutter build with --analyze-size to identify large components."
        },
        {
            "instruction": "What is the purpose of RepaintBoundary in Flutter performance optimization?",
            "input": "",
            "output": "RepaintBoundary creates a separate rendering layer for its child, isolating it from repaints of the surrounding widget tree. Without it, when any widget in a layer repaints, all widgets in that layer are repainted. Wrapping frequently repainting widgets (animations, timers) in RepaintBoundary prevents unnecessary repaints of static content, significantly improving rendering performance."
        },
        {
            "instruction": "What is jank in Flutter and how do you identify it?",
            "input": "",
            "output": "Jank is visible stuttering or frame drops in the UI, occurring when frames take longer than 16ms (for 60fps) to render. It is identified using Flutter DevTools' Performance view, which shows frame rendering times with red bars for jank frames. The timeline separates UI thread work (build/layout) from raster thread work (painting), helping pinpoint the bottleneck source."
        },
        {
            "instruction": "What is shader compilation jank in Flutter?",
            "input": "",
            "output": "Shader compilation jank occurs when Flutter compiles Skia shaders on-the-fly during first-time animations, causing brief freezes. It typically happens only on first run. Mitigation strategies include: using flutter build with --bundle-sksl-warmup to capture and pre-warm shaders, running the app in profile mode to collect SkSL shaders, and using Impeller rendering engine on iOS which pre-compiles all shaders."
        },
        # Platform Channels Deep Dive
        {
            "instruction": "How do platform channels work internally in Flutter?",
            "input": "",
            "output": "Platform channels use binary message passing between Dart and native code. Messages are encoded using StandardMethodCodec into ByteData, sent through the engine's native binding, decoded on the receiving side, processed, and the result is sent back. MethodChannel handles request-response patterns, EventChannel handles continuous event streams, and BasicMessageChannel handles raw messages."
        },
        {
            "instruction": "What is an EventChannel in Flutter?",
            "input": "",
            "output": "EventChannel is a platform channel for receiving a continuous stream of events from native code. On the native side, a StreamHandler provides onListen (to start sending events) and onCancel (to stop). On the Dart side, EventChannel.receiveBroadcastStream() returns a Stream that emits events as they arrive. It is used for sensor data, location updates, and connectivity changes."
        },
        {
            "instruction": "What is the Pigeon package for Flutter platform channels?",
            "input": "",
            "output": "Pigeon is a code generation tool that creates type-safe platform channel interfaces from a Dart API definition. Instead of manually writing MethodChannel string-based calls, Pigeon generates Dart, Kotlin/Java, and Swift/Objective-C code with strongly typed methods and data classes. This eliminates runtime errors from mismatched method names or argument types."
        },
        # Testing Deep Dive
        {
            "instruction": "How do you write unit tests in Flutter?",
            "input": "",
            "output": "Unit tests in Flutter use the test package with test() and group() functions. Tests follow the Arrange-Act-Assert pattern: set up objects, perform actions, and verify results using expect() with matchers. Mock dependencies using mockito with @GenerateMocks annotation. Run tests with 'flutter test'. Good unit tests are fast, isolated, and test a single behavior."
        },
        {
            "instruction": "How do you mock dependencies in Flutter tests?",
            "input": "",
            "output": "Dependencies are mocked in Flutter using the mockito package. Annotate test files with @GenerateMocks([ClassName]) and run build_runner to generate mock classes. Use when() to stub method returns and verify() to check method calls. For simple cases, create manual mock classes implementing the interface. mocktail is an alternative that doesn't require code generation."
        },
        {
            "instruction": "What is integration testing in Flutter?",
            "input": "",
            "output": "Integration testing in Flutter verifies complete app flows on a real device or emulator. Tests use the integration_test package and run with 'flutter test integration_test/'. They use WidgetTester like widget tests but run on actual devices, testing real navigation, network calls, and platform interactions. They are slower but validate end-to-end functionality."
        },
        {
            "instruction": "What is the golden test in Flutter?",
            "input": "",
            "output": "Golden tests (screenshot tests) capture a widget's rendered appearance and compare it against a saved reference image (the 'golden' file). They detect unintended visual changes like layout shifts or styling bugs. Use matchesGoldenFile() matcher to compare. Golden files are updated with --update-goldens flag. They are useful for ensuring visual consistency across code changes."
        },
        {
            "instruction": "How do you test async code in Flutter?",
            "input": "",
            "output": "Async code in Flutter is tested using async test functions with await. For Futures, use expectLater() with completion matchers or await the Future directly. For Streams, use emitsInOrder(), emits(), and neverEmits() matchers. Use fake async with fakeAsync() from package:fake_async to control time-dependent code without real delays, advancing time with elapse()."
        },
        # Architecture Patterns
        {
            "instruction": "What is the MVVM pattern in Flutter?",
            "input": "",
            "output": "MVVM (Model-View-ViewModel) separates UI (View), business logic (ViewModel), and data (Model). In Flutter, Views are widgets that observe the ViewModel, ViewModels are ChangeNotifiers or Bloc/Cubit classes that expose state and actions, and Models represent data entities. The View binds to ViewModel state reactively, and the ViewModel manipulates Models without knowing about the View."
        },
        {
            "instruction": "What is clean architecture in Flutter?",
            "input": "",
            "output": "Clean architecture in Flutter organizes code into concentric layers: Domain (entities, use cases, repository interfaces), Data (API clients, database, repository implementations), and Presentation (UI, state management). Dependencies point inward — outer layers depend on inner layers through abstractions. This ensures testability, separation of concerns, and independence from external frameworks."
        },
        {
            "instruction": "What is dependency injection in Flutter?",
            "input": "",
            "output": "Dependency injection (DI) is a pattern where objects receive their dependencies from external sources rather than creating them internally. In Flutter, DI is implemented through constructor injection, Provider/Riverpod for widget-tree-scoped injection, GetIt as a service locator, or injectable package for code-generated DI. DI improves testability by allowing mock substitution."
        },
        {
            "instruction": "What is the Repository pattern in Flutter?",
            "input": "",
            "output": "The Repository pattern abstracts data access behind an interface, separating business logic from data sources. A repository interface in the domain layer defines methods like getUsers(), while concrete implementations in the data layer fetch from API, database, or cache. This allows swapping data sources without changing business logic and simplifies testing with mock repositories."
        },
        # CI/CD
        {
            "instruction": "How do you set up CI/CD for a Flutter project?",
            "input": "",
            "output": "Flutter CI/CD can be set up using GitHub Actions, GitLab CI, Codemagic, or Fastlane. A typical pipeline includes: linting (flutter analyze), running tests (flutter test), building the app (flutter build apk/ipa), and deploying to stores. Codemagic provides Flutter-specific workflows. GitHub Actions uses the subosito/flutter-action for environment setup. Fastlane automates store submissions."
        },
        {
            "instruction": "What is Codemagic in Flutter development?",
            "input": "",
            "output": "Codemagic is a CI/CD platform specifically designed for Flutter and mobile app development. It provides automated building, testing, and publishing of Flutter apps to App Store and Play Store. It supports custom build scripts, environment variables, code signing, automated versioning, and integration with various notification services. It offers both YAML-based and GUI-based workflow configuration."
        },
        # Advanced Dart
        {
            "instruction": "What are records in Dart?",
            "input": "",
            "output": "Records are anonymous, immutable aggregate types introduced in Dart 3.0. They allow grouping multiple values without creating a class. Defined with parentheses like (int, String) for positional, or ({int age, String name}) for named fields. They support destructuring: var (a, b) = getRecord(). Records have value equality — two records with the same fields and values are equal."
        },
        {
            "instruction": "What are sealed classes in Dart?",
            "input": "",
            "output": "Sealed classes, introduced in Dart 3.0, restrict which classes can extend or implement them — subclasses must be in the same library. This enables exhaustive pattern matching in switch expressions, where the compiler ensures all subtypes are handled. Sealed classes are ideal for representing finite state types like Result<Success, Failure> or UI states (Loading, Data, Error)."
        },
        {
            "instruction": "What is pattern matching in Dart?",
            "input": "",
            "output": "Pattern matching, introduced in Dart 3.0, enables destructuring and matching values against patterns in switch statements, if-case, and variable declarations. Supported patterns include constant, variable, wildcard (_), list, map, record, object, and logical patterns with && and ||. It enables concise, readable code for complex data processing and type-safe state handling."
        },
        {
            "instruction": "What are Dart zones?",
            "input": "",
            "output": "Zones are execution contexts in Dart that provide error handling, scheduling control, and intercepting of async operations. runZonedGuarded() creates a zone that catches all uncaught async errors. Zones can override print(), Timer creation, and microtask scheduling. Flutter uses a root zone for framework initialization, and zones are useful for error reporting libraries like Sentry."
        },
        # Advanced Flutter
        {
            "instruction": "What is the Impeller rendering engine in Flutter?",
            "input": "",
            "output": "Impeller is Flutter's next-generation rendering engine replacing Skia on iOS (default since Flutter 3.16) and in development for Android. It pre-compiles all shaders during build time, eliminating first-frame shader compilation jank. Impeller uses Metal on iOS and Vulkan/OpenGL on Android, providing smoother animations and more predictable rendering performance."
        },
        {
            "instruction": "What is the Flutter rendering pipeline?",
            "input": "",
            "output": "The Flutter rendering pipeline follows these stages: User Input → Animation → Build (widget tree creation) → Layout (size and position calculation using RenderObject constraints) → Paint (drawing commands using Canvas) → Compositing (layer tree assembly) → Rasterization (GPU renders pixels). This pipeline runs at 60/120fps, with the UI thread handling build through compositing and the raster thread handling GPU rendering."
        },
        {
            "instruction": "What is the difference between AOT and JIT compilation in Flutter?",
            "input": "",
            "output": "JIT (Just-In-Time) compilation is used in debug mode — it compiles code on-the-fly, enabling hot reload and faster development cycles but with slower runtime performance. AOT (Ahead-of-Time) compilation is used in release mode — it compiles Dart to native machine code before execution, providing fast startup, consistent performance, and smaller memory footprint at the cost of longer build times."
        },
        {
            "instruction": "What is the key difference between method channels and FFI in Flutter?",
            "input": "",
            "output": "Method channels use asynchronous message passing between Dart and platform code, requiring serialization/deserialization and running on the platform thread. Dart FFI (Foreign Function Interface) directly calls native C/C++ functions synchronously from Dart without platform channel overhead. FFI is faster and suitable for compute-intensive native libraries, while method channels are better for platform-specific API access."
        },
        {
            "instruction": "What is Dart FFI?",
            "input": "",
            "output": "Dart FFI (Foreign Function Interface) allows Dart code to call C functions directly. It uses the dart:ffi library to load dynamic libraries (.so, .dylib, .dll), define function signatures using NativeFunction types, and call them synchronously. FFI is used for accessing native libraries, crypto operations, image processing, and other performance-sensitive native code without platform channel overhead."
        },
        {
            "instruction": "How does Flutter handle memory management?",
            "input": "",
            "output": "Flutter uses Dart's garbage collector for memory management. Dart employs a generational garbage collection strategy with a young generation space (fast allocation, frequent minor GC) and an old generation space (promoted long-lived objects, infrequent major GC). Flutter also manages GPU memory for textures and layers. Memory leaks commonly occur from undisposed controllers, uncancelled subscriptions, and circular references."
        },
        {
            "instruction": "What are DevTools memory profiling capabilities?",
            "input": "",
            "output": "Flutter DevTools Memory view provides heap snapshots showing live objects by class, allocation tracks showing what's being created, a memory timeline showing Dart/native/graphics memory usage over time, and a diff view comparing two snapshots to identify leaks. You can filter by class, trace allocation call stacks, and identify retained objects that prevent garbage collection."
        },
        {
            "instruction": "What is the Skia rendering engine?",
            "input": "",
            "output": "Skia is an open-source 2D graphics library that Flutter uses for rendering. It provides drawing APIs for shapes, text, images, and effects that work across platforms. Skia compiles shaders just-in-time during runtime, which can cause initial jank. On iOS, Flutter is transitioning from Skia to Impeller, which pre-compiles shaders for smoother performance."
        },
        {
            "instruction": "How do you implement deep linking in Flutter?",
            "input": "",
            "output": "Deep linking in Flutter requires platform-specific setup (Android App Links, iOS Universal Links) and Dart-side route handling. On Android, configure intent filters in AndroidManifest.xml. On iOS, set Associated Domains in Xcode. In Flutter, use Navigator 2.0's RouterDelegate or packages like go_router to parse incoming URIs and navigate to the appropriate screen."
        },
        {
            "instruction": "What is the purpose of the flutter_driver package?",
            "input": "",
            "output": "flutter_driver was the original integration testing framework for Flutter (now largely replaced by integration_test). It runs tests in a separate process that communicates with the app via a JSON-RPC protocol. It supports finding widgets, scrolling, entering text, taking screenshots, and measuring performance. The newer integration_test package is recommended as it runs in the same process for easier setup."
        },
        {
            "instruction": "What is code generation in Flutter and when is it used?",
            "input": "",
            "output": "Code generation uses build_runner to automatically generate Dart code from annotations. Common use cases include: json_serializable for JSON parsing boilerplate, freezed for immutable data classes with unions, mockito for test mocks, injectable for dependency injection, auto_route for navigation, and retrofit for type-safe API clients. Run with 'dart run build_runner build'."
        },
        {
            "instruction": "What is the freezed package in Flutter?",
            "input": "",
            "output": "Freezed is a code generation package that creates immutable data classes with value equality, copyWith, serialization, and union types. Annotate a class with @freezed and define factory constructors. It generates toString, ==, hashCode, copyWith, and optionally fromJson/toJson. Union types enable sealed-class-like pattern matching for states like AsyncValue(loading, data, error)."
        },
        {
            "instruction": "How do you handle flavors/variants in Flutter?",
            "input": "",
            "output": "Flavors in Flutter create different app variants (dev, staging, production) with different configurations, API endpoints, and app IDs. On Android, configure productFlavors in build.gradle. On iOS, use Xcode schemes and configurations. Use --flavor flag with flutter run/build. In Dart, use String.fromEnvironment or dedicated config files to access flavor-specific values at runtime."
        },
        {
            "instruction": "What is the purpose of the flutter_lints package?",
            "input": "",
            "output": "flutter_lints (now flutter_lints is superseded by the officially recommended lints package) provides a set of recommended lint rules for Flutter projects. Configured in analysis_options.yaml, it enforces coding best practices like preferring const constructors, using proper typing, and avoiding common mistakes. Custom rules can be added or existing ones overridden in the analysis options file."
        },
        {
            "instruction": "What is ProGuard/R8 and how does it relate to Flutter?",
            "input": "",
            "output": "ProGuard and R8 are code shrinking and obfuscation tools for Android. R8 (the default) reduces APK size by removing unused Java/Kotlin code and obfuscating class/method names. In Flutter, R8 affects the native Android portion of the app. Configure it in android/app/build.gradle with minifyEnabled true. ProGuard rules may be needed to preserve classes used by plugins."
        },
        {
            "instruction": "What is the purpose of the Completer class in Dart?",
            "input": "",
            "output": "Completer is a class that creates a Future and provides the ability to complete it later with a value or error. It is useful when you need to convert callback-based APIs into Future-based APIs. You create a Completer, return completer.future, and call completer.complete(value) or completer.completeError(error) when the result is available. Each Completer can only be completed once."
        },
        {
            "instruction": "What is the Equatable package in Flutter?",
            "input": "",
            "output": "Equatable is a Dart package that simplifies value equality implementation. By extending Equatable and listing properties in the props getter, the package automatically generates == and hashCode. This eliminates boilerplate code for classes that need value-based comparison, commonly used with Bloc states and events, data transfer objects, and entity classes."
        },
        {
            "instruction": "How does Flutter handle accessibility?",
            "input": "",
            "output": "Flutter handles accessibility through the Semantics tree, which provides information to platform accessibility services (TalkBack on Android, VoiceOver on iOS). Material widgets have built-in semantic annotations. Custom widgets use the Semantics widget to add labels, hints, and actions. Flutter DevTools provides a Semantics debugger. Key practices include meaningful labels, focus ordering, and sufficient color contrast."
        },
        {
            "instruction": "What is the difference between hot reload, hot restart, and full restart?",
            "input": "",
            "output": "Hot reload injects updated code into the running Dart VM preserving state — fastest but doesn't apply to some changes. Hot restart resets the app state (calling main() again) while keeping the VM running — applies to global variable and static field changes. Full restart stops the VM completely and rebuilds the app from scratch — needed for native code changes and plugin additions."
        },
        {
            "instruction": "What is a BuildOwner in Flutter?",
            "input": "",
            "output": "BuildOwner manages the build lifecycle for a widget tree. It tracks widgets that need rebuilding, processes the dirty elements list during each frame, and handles the build phase ordering. In typical apps, there is one BuildOwner managed by the WidgetsBinding. It is responsible for the scheduleBuildFor() call that marks elements dirty and processes them during the build phase."
        },
        {
            "instruction": "What is the purpose of InheritedModel in Flutter?",
            "input": "",
            "output": "InheritedModel is a specialized InheritedWidget that allows dependents to subscribe to specific aspects of the model rather than the entire widget. This optimizes rebuild performance by only notifying widgets that depend on the changed aspect. Widgets use InheritedModel.inheritFrom with an aspect parameter, and updateShouldNotifyDependent checks only the relevant aspects."
        },
        {
            "instruction": "What is the purpose of WidgetsBindingObserver in Flutter?",
            "input": "",
            "output": "WidgetsBindingObserver is a mixin for observing app lifecycle events and system changes. It provides callbacks for didChangeAppLifecycleState (foreground/background), didChangeMetrics (screen size changes), didChangePlatformBrightness (light/dark mode), and didChangeLocales. Mix it into a State class, register with WidgetsBinding.instance.addObserver, and unregister in dispose."
        },
        {
            "instruction": "How do you implement background tasks in Flutter?",
            "input": "",
            "output": "Background tasks in Flutter use different approaches depending on the use case: workmanager package for scheduled background tasks following platform constraints, flutter_background_service for long-running background services, Isolates for compute-heavy tasks within the app, and platform channels to invoke native background services. iOS has strict background execution limits compared to Android."
        },
        {
            "instruction": "What is the purpose of the RestorationMixin in Flutter?",
            "input": "",
            "output": "RestorationMixin enables state restoration when the OS kills and recreates the app (common on Android). It uses RestorableProperty objects (RestorableInt, RestorableString, etc.) to automatically save and restore widget state. When the app is recreated, the framework restores these values from the saved state bundle, providing a seamless experience to the user."
        },
        {
            "instruction": "What is Method Channel codec in Flutter?",
            "input": "",
            "output": "Method Channel codecs handle serialization and deserialization of messages between Dart and platform code. StandardMethodCodec (default) uses StandardMessageCodec for binary encoding, supporting null, bool, int, double, String, byte data, lists, and maps. JSONMethodCodec uses JSON format. Custom codecs can be created for specialized data types by extending MethodCodec."
        },
        {
            "instruction": "What is the purpose of the ValueListenableBuilder widget?",
            "input": "",
            "output": "ValueListenableBuilder rebuilds its subtree when a ValueListenable (typically ValueNotifier) changes value. It is a lightweight reactive widget that doesn't require a state management package. It takes a valueListenable, a builder function that receives the current value, and an optional child that is not rebuilt. It is ideal for simple reactive UI updates with minimal overhead."
        },
        {
            "instruction": "How do you handle network connectivity in Flutter?",
            "input": "",
            "output": "Network connectivity in Flutter is handled using the connectivity_plus package, which provides connectivity status (WiFi, mobile, none) via a stream and one-time checks. For actual internet reachability verification (not just network interface), you can make a lightweight HTTP request or DNS lookup. The stream enables reactive UI updates when connectivity changes."
        },
        {
            "instruction": "What is the purpose of AutomaticKeepAliveClientMixin?",
            "input": "",
            "output": "AutomaticKeepAliveClientMixin prevents a widget's state from being disposed when it scrolls off-screen in a lazy list or PageView. By mixing it into a State class and overriding wantKeepAlive to return true, the framework keeps the state alive. You must call super.build(context) in your build method. It is useful for preserving expensive-to-rebuild content in tabs or lists."
        },
        {
            "instruction": "What is the purpose of the Notification system in Flutter?",
            "input": "",
            "output": "Flutter's Notification system allows widgets to bubble information up the widget tree without direct references. A Notification dispatched via dispatch(context) travels upward and can be caught by NotificationListener widgets. Common built-in notifications include ScrollNotification, LayoutChangedNotification, and SizeChangedLayoutNotification. Custom notifications extend Notification class."
        },
        {
            "instruction": "What is the CompositedTransformTarget and CompositedTransformFollower pattern?",
            "input": "",
            "output": "CompositedTransformTarget and CompositedTransformFollower are widgets that link two widgets' positions across the layer tree using a LayerLink. The follower positions itself relative to the target regardless of their positions in the widget tree. This pattern is used for creating overlays like tooltips, dropdown menus, and autocomplete suggestions that follow their anchor widget."
        },
        {
            "instruction": "How do you implement Firebase integration in Flutter?",
            "input": "",
            "output": "Firebase integration uses the FlutterFire packages. Initialize with Firebase CLI (flutterfire configure) to generate platform config. Add firebase_core and specific packages (firebase_auth, cloud_firestore, etc.) to pubspec.yaml. Call Firebase.initializeApp() in main(). Each service has its own API — Firestore for database, Auth for authentication, Storage for files, and Messaging for push notifications."
        },
        {
            "instruction": "What is the purpose of the debugPrint function in Flutter?",
            "input": "",
            "output": "debugPrint is a throttled version of print() that prevents log output from being dropped when multiple lines are printed rapidly. The standard print() can lose output when the system logger buffer fills up, but debugPrint rate-limits output to prevent this. It is recommended over print() for debug logging in Flutter apps. It is stripped from release builds."
        },
        {
            "instruction": "What are the different types of keys in Flutter and when should each be used?",
            "input": "",
            "output": "ValueKey uses a value for equality (ideal for list items with unique IDs). ObjectKey uses object identity. UniqueKey is always unique (forces widget recreation). GlobalKey is unique across the entire app (for accessing State from outside). PageStorageKey preserves scroll position. Use keys when reordering list items, animating list changes, or preserving state across widget moves."
        },
        # ─── Additional Advanced Questions ─────────────────────────────
        {
            "instruction": "How does Flutter's rendering pipeline work internally?",
            "input": "",
            "output": "Flutter's rendering pipeline processes frames through phases: 1) Animation — tick animations and microtasks, 2) Build — run build methods for dirty widgets and create/update Elements, 3) Layout — walk the RenderObject tree computing sizes and positions via performLayout(), 4) Compositing — organize layers into a scene, 5) Paint — paint each RenderObject onto its layer via paint(), 6) Rasterize — convert the layer tree to pixels on the GPU. The pipeline is driven by the engine's vsync signals at 60/120fps."
        },
        {
            "instruction": "How does the Dart VM handle memory management and garbage collection?",
            "input": "",
            "output": "Dart uses generational garbage collection with two generations: young (new space) and old. Young space uses semi-space scavenging — fast but pauses the mutator briefly. It copies live objects to the other semi-space. Old space uses concurrent mark-sweep — marks reachable objects concurrently, then sweeps unreachable ones. Objects that survive young-space collections are promoted to old space. The GC is designed for low-latency UI threads."
        },
        {
            "instruction": "How does tree shaking work in Flutter?",
            "input": "",
            "output": "Tree shaking removes unused code during AOT compilation for release builds. The Dart compiler performs whole-program analysis, starting from main() and tracing all reachable code. Unreachable functions, classes, and methods are eliminated from the final binary. Icons are also tree-shaken if unused. Conditional imports and deferred loading affect what code is included. Tree shaking significantly reduces app size."
        },
        {
            "instruction": "How does Dart's AOT compilation differ from JIT for Flutter apps?",
            "input": "",
            "output": "JIT (Just-In-Time) compiles Dart code during runtime, enabling hot reload and debugging — used in debug mode. AOT (Ahead-Of-Time) compiles Dart to native machine code before deployment — used in release mode. JIT is faster to iterate but slower to execute with larger binary. AOT produces optimized native code with smaller binary, faster startup, predictable performance, and no compilation overhead."
        },
        {
            "instruction": "How do you implement custom RenderObjects in Flutter?",
            "input": "",
            "output": "Custom RenderObjects control layout, painting, and hit testing directly. Create a RenderBox subclass, override performLayout() to compute size and position children, paint() to draw using Canvas, and hitTestSelf/hitTestChildren for gesture detection. Create a corresponding SingleChildRenderObjectWidget or MultiChildRenderObjectWidget that creates and updates the RenderObject. This bypasses the framework layer for maximum control."
        },
        {
            "instruction": "How does Flutter's Element recycling optimize performance?",
            "input": "",
            "output": "When Flutter encounters a new widget during reconciliation, it first checks if the existing element can be updated (same runtimeType and key). If yes, it updates the element with the new widget — reusing the existing RenderObject and subtree. If not, it deactivates the old element and creates a new one. For lists, keys enable element reuse across reorders. This minimizes expensive RenderObject creation."
        },
        {
            "instruction": "How do you create a custom sliver in Flutter?",
            "input": "",
            "output": "Custom slivers extend RenderSliver and override performLayout() to compute scroll extent, paint extent, and child positioning. The geometry is set via SliverGeometry. Constraints come as SliverConstraints (scrollOffset, remainingPaintExtent, crossAxisExtent). Create a companion widget extending RenderObjectWidget with createRenderObject/updateRenderObject. Use SliverMultiBoxAdaptorWidget for slivers with multiple box children."
        },
        {
            "instruction": "How do you implement Dart FFI (Foreign Function Interface)?",
            "input": "",
            "output": "Dart FFI (dart:ffi) calls native C/C++ functions directly without platform channels. Define native function signatures using NativeFunction typedef, load the dynamic library with DynamicLibrary.open(), look up functions with lookupFunction<NativeFunction, DartFunction>(). Pass/receive primitives, Pointers, and Structs. ffigen generates Dart bindings from C headers automatically. FFI has lower latency than MethodChannel."
        },
        {
            "instruction": "How do isolates communicate using SendPort and ReceivePort?",
            "input": "",
            "output": "ReceivePort creates a message inbox and provides a SendPort for sending messages to it. The spawning isolate creates a ReceivePort, passes its SendPort to Isolate.spawn(). The spawned isolate receives this SendPort and can send messages back. For bidirectional communication, the spawned isolate creates its own ReceivePort and sends its SendPort back. Messages are deep-copied between isolates."
        },
        {
            "instruction": "How do you implement background processing in Flutter?",
            "input": "",
            "output": "Background processing uses: Isolate.run() for heavy computation off the main thread, workmanager package for periodic background tasks (even when app is killed), flutter_background_service for long-running foreground services, and firebase_messaging onBackgroundMessage for push notifications. On Android, background execution has restrictions — use foreground services for reliable execution."
        },
        {
            "instruction": "How does Flutter's layer system work?",
            "input": "",
            "output": "Flutter organizes painting into a tree of Layer objects. OpacityLayer applies transparency, TransformLayer applies transforms, ClipRectLayer clips, OffsetLayer positions children, and PictureLayer contains actual drawing commands. Layers are composited into a Scene sent to the engine. RepaintBoundary creates a new OffsetLayer, enabling independent repainting of subtrees. The layer tree enables efficient compositing on the GPU."
        },
        {
            "instruction": "What is the Impeller rendering engine in Flutter?",
            "input": "",
            "output": "Impeller is Flutter's new rendering engine replacing Skia on iOS (default since Flutter 3.16) and Android (preview). It pre-compiles all shader programs during build time, eliminating shader compilation jank (first-frame stuttering). It uses Metal on iOS and Vulkan/OpenGL on Android. Impeller provides more predictable performance with consistent frame rates and reduced memory usage."
        },
        {
            "instruction": "How do you profile and optimize Flutter app performance?",
            "input": "",
            "output": "Use Flutter DevTools Performance view to identify jank. Profile mode (flutter run --profile) provides production-like performance with debugging tools. Common optimizations: const constructors to avoid rebuilds, RepaintBoundary for isolated repainting, ListView.builder for lazy loading, pre-computed layouts, cached images, reduced widget depth, and avoiding expensive operations in build methods."
        },
        {
            "instruction": "How do you reduce Flutter app size?",
            "input": "",
            "output": "App size reduction: use --split-debug-info to extract debug symbols, enable --obfuscate for release builds, use deferred components for features loaded on demand, remove unused packages, compress assets, use SVG instead of PNG where possible, enable ProGuard/R8 on Android, remove unused Material icons with tree shaking, analyze size with --analyze-size flag."
        },
        {
            "instruction": "How does the Provider.select method optimize rebuilds?",
            "input": "",
            "output": "Provider.select rebuilds the consumer widget only when a specific derived value changes, not when any property of the provided object changes. context.select<Model, String>((model) => model.name) rebuilds only when name changes. Without select, Consumer rebuilds on any model change. Selector widget provides the same optimization declaratively. This prevents unnecessary rebuilds in complex models."
        },
        {
            "instruction": "How do you implement multi-window support in Flutter desktop?",
            "input": "",
            "output": "Flutter desktop multi-window support is still evolving. The approach involves creating multiple Flutter engine instances with separate entry points, or using platform-specific native code to manage windows with MethodChannel communication between them. The desktop_multi_window package provides a simpler API. Each window can have its own widget tree, state, and size."
        },
        {
            "instruction": "How do you implement Flutter web SEO optimization?",
            "input": "",
            "output": "Flutter web SEO challenges arise because content is rendered in Canvas. Solutions: use HTML renderer (--web-renderer html) for text-based content, add meta tags in index.html, implement server-side rendering of critical content, use semantic HTML elements via HtmlElementView, provide a sitemap.xml, and use the url_strategy package for clean URLs without hash fragments."
        },
        {
            "instruction": "How do you implement advanced platform channel communication?",
            "input": "",
            "output": "Advanced platform channels use: BasicMessageChannel for bidirectional asynchronous messages with codecs (StandardMessageCodec, JSONMessageCodec, BinaryCodec), MethodChannel for method calls, EventChannel for streaming. Custom codecs extend StandardMessageCodec for type-safe serialization. Pigeon package generates type-safe platform channel code from a DSL, eliminating manual serialization."
        },
        {
            "instruction": "What is the Pigeon package for Flutter platform channels?",
            "input": "",
            "output": "Pigeon generates type-safe platform channel interfaces from a Dart API definition. Define messages and host/flutter APIs in a Pigeon file, run the generator to produce Dart, Kotlin/Java, Swift/Objective-C code. Generated code handles serialization, method dispatch, and error handling. This eliminates string-based method names and manual codec implementation, reducing platform channel bugs."
        },
        {
            "instruction": "How do you implement a plugin package in Flutter?",
            "input": "",
            "output": "Create a plugin with 'flutter create --template=plugin --platforms=android,ios plugin_name'. The plugin has: Dart API in lib/, Android implementation in android/ (Kotlin), iOS implementation in ios/ (Swift), federated platform interface in platform_interface package. Use MethodChannel or FFI for platform communication. Register the plugin in pubspec.yaml with pluginClass. Test on each platform."
        },
        {
            "instruction": "What is federated plugin architecture in Flutter?",
            "input": "",
            "output": "Federated plugins split platform implementations into separate packages: app-facing package (public API), platform_interface package (abstract contract), and platform-specific packages (android, ios, web implementations). This allows third parties to add platform support without modifying the original plugin. Each platform package implements the platform interface and is registered via Dart's default factory mechanism."
        },
        {
            "instruction": "How do you implement CI/CD for Flutter projects?",
            "input": "",
            "output": "Flutter CI/CD uses GitHub Actions, GitLab CI, Bitrise, or Codemagic. Pipeline stages: 1) Install Flutter SDK, 2) flutter pub get, 3) flutter analyze (lint), 4) flutter test (unit/widget tests), 5) flutter build (APK/IPA/web), 6) Deploy (Firebase App Distribution, TestFlight, Play Store). Use Fastlane for automated signing and deployment. Cache pub dependencies for speed."
        },
        {
            "instruction": "How does Flutter handle accessibility?",
            "input": "",
            "output": "Flutter provides accessibility through the Semantics widget tree. Built-in widgets include semantic labels automatically. Custom widgets need Semantics annotation with label, hint, value, and flags (isButton, isHeader). Enable large text via MediaQuery.textScaleFactorOf. Ensure sufficient color contrast. Test with TalkBack (Android) and VoiceOver (iOS). Use SemanticsDebugger for visual representation."
        },
        {
            "instruction": "How do you implement advanced Dart generics?",
            "input": "",
            "output": "Advanced Dart generics include: bounded generics (T extends Comparable<T>) to constrain types, covariant keyword for type-safe overrides, generic methods on classes (R transform<R>(R Function(T) fn)), generic type aliases (typedef Cache<T> = Map<String, T>), and reified generics (Dart retains type information at runtime unlike Java's type erasure)."
        },
        {
            "instruction": "How do you implement custom lint rules for Flutter?",
            "input": "",
            "output": "Custom lint rules use the custom_lint package with the analyzer plugin API. Create a package that extends LintRule, implement the visitMethodInvocation/visitClassDeclaration methods to detect issues, and register fixes. Configure in analysis_options.yaml with analyzer: plugins: [custom_lint]. Use dart_code_metrics for pre-built complexity and design metrics. DCM provides coupling, complexity, and size metrics."
        },
        {
            "instruction": "How do you implement the Command pattern in Flutter?",
            "input": "",
            "output": "The Command pattern encapsulates operations as objects with execute(), undo(), and optional redo() methods. In Flutter, this enables undo/redo functionality: maintain a command history stack, push commands on execution, pop on undo. Commands store the state needed to reverse their action. Use with text editors, drawing apps, and any app requiring operation reversal."
        },
        {
            "instruction": "How do you implement compile-time safety for routes in Flutter?",
            "input": "",
            "output": "Compile-time route safety prevents navigation errors. Use code-generated routes with auto_route (annotated page classes → typed route classes), or go_router_builder for GoRouter type-safe routes. Define routes as classes with typed parameters: context.pushRoute(UserRoute(id: 42)). The compiler catches missing parameters and type mismatches at build time instead of runtime crashes."
        },
        {
            "instruction": "How does Dart's zone system work?",
            "input": "",
            "output": "Zones in Dart provide an execution context for asynchronous operations. They can intercept and transform: timer creation (scheduleMicrotask), error handling (uncaught errors), print output, and async callbacks. runZonedGuarded captures uncaught async errors. Flutter's framework runs in a zone to catch and report errors. Zones enable features like async stack traces and centralized error logging."
        },
        {
            "instruction": "How do you implement method cascading and pipeline patterns in Dart?",
            "input": "",
            "output": "Dart's cascade operator (..) allows multiple operations on the same object without repeating the reference: list..add(1)..add(2)..sort(). The null-aware cascade (?...) handles nullable objects. For pipeline patterns, use extension methods to add chainable operations: 'hello'.capitalize().addSuffix('!'). combine with collection methods: list.where().map().toList() for functional pipelines."
        },
        {
            "instruction": "How do you implement advanced error boundaries in Flutter?",
            "input": "",
            "output": "Error boundaries catch and display errors gracefully. Set ErrorWidget.builder for custom error screens in production. Use FlutterError.onError for framework errors (widget build, layout, paint). PlatformDispatcher.instance.onError catches uncaught async errors. runZonedGuarded provides zone-level error capture. Report errors to services like Sentry or Crashlytics. Show user-friendly error UIs instead of red screens."
        },
        {
            "instruction": "How do you implement advanced theming with ThemeExtension?",
            "input": "",
            "output": "ThemeExtension allows adding custom theme properties beyond ThemeData's built-in properties. Create a class extending ThemeExtension<T> with custom fields, override copyWith() and lerp() for animation support. Register via ThemeData(extensions: [MyTheme()]). Access via Theme.of(context).extension<MyTheme>(). This enables app-specific theme properties like custom spacing, brand colors, and component styles."
        },
        {
            "instruction": "How do you optimize image loading in Flutter?",
            "input": "",
            "output": "Image optimization: use cached_network_image for caching with placeholder/error widgets, ResizeImage to decode at display size (reducing memory), precacheImage for pre-loading, FadeInImage for smooth loading transitions, Image.memory for byte data, set cacheHeight/cacheWidth on Image for memory-efficient decoding. Use WebP format for smaller file sizes. Implement lazy loading for image-heavy lists."
        },
        {
            "instruction": "How does Flutter handle compositing and GPU rendering?",
            "input": "",
            "output": "Flutter creates a Layer tree during painting. Layers are composited into a Scene object sent to the engine. The engine uses Skia (or Impeller) to rasterize the scene on the GPU. Compositing optimizes by: caching layer contents, avoiding full repaint via RepaintBoundary layers, hardware-accelerating opacity/transform/clip operations, and batching draw calls. The GPU thread runs separately from the UI thread."
        },
        {
            "instruction": "How do you implement custom implicit animation widgets?",
            "input": "",
            "output": "Custom implicit animations extend ImplicitlyAnimatedWidget. Override forEachTween() to register tween properties. In the State class, extend ImplicitlyAnimatedWidgetState, override forEachTween() to create/update tweens, and use evaluate(tween) in build() to get animated values. The framework handles AnimationController lifecycle. This pattern creates widgets that animate property changes automatically."
        },
        {
            "instruction": "How do you implement physics-based animations in Flutter?",
            "input": "",
            "output": "Physics-based animations use Simulation classes with AnimationController.animateWith(). SpringSimulation creates spring/bounce effects with mass, stiffness, and damping. FrictionSimulation creates deceleration. GravitySimulation simulates gravity. ClampedSimulation bounds simulations. These produce natural-feeling animations that respond to velocity and force rather than fixed durations and curves."
        },
        {
            "instruction": "What is the WidgetsBindingObserver mixin used for?",
            "input": "",
            "output": "WidgetsBindingObserver listens to app lifecycle and system events. Override didChangeAppLifecycleState for app state changes (resumed, paused, inactive, detached, hidden). didChangeMetrics for screen size/rotation changes. didChangePlatformBrightness for theme mode changes. didChangeLocales for locale changes. didHaveMemoryPressure for memory warnings. Mix into State and register with WidgetsBinding.instance.addObserver."
        },
        {
            "instruction": "How do you implement secure data storage in Flutter?",
            "input": "",
            "output": "Secure storage uses flutter_secure_storage backed by Keychain (iOS) and EncryptedSharedPreferences (Android). For sensitive SQLite data, use sqflite with sqlcipher_flutter_libs for encryption. Never store secrets in SharedPreferences, assets, or source code. Use server-side token rotation, certificate pinning with http_certificate_pinning, and proper key management. Hash passwords with bcrypt, never store plaintext."
        },
        {
            "instruction": "How do you implement SSL pinning in Flutter?",
            "input": "",
            "output": "SSL/certificate pinning prevents MITM attacks by validating the server's certificate against a known certificate or public key. Implement with Dio's httpClientAdapter by setting SecurityContext with trusted certificates, or use the http_certificate_pinning package. Pin the public key hash rather than the certificate for easier rotation. Handle certificate expiration gracefully."
        },
        {
            "instruction": "How do you prevent reverse engineering of Flutter apps?",
            "input": "",
            "output": "Protect Flutter apps with: --obfuscate flag to obfuscate Dart code, --split-debug-info to separate debug symbols, ProGuard/R8 for Android Java/Kotlin code, code signing and integrity checks, server-side validation for critical logic, encrypted local storage, tamper detection using platform-specific APIs, and avoiding hardcoded secrets. No technique is foolproof — defense in depth is key."
        },
        {
            "instruction": "How does Flutter handle state management at scale?",
            "input": "",
            "output": "At scale, state management requires: separation of global app state (auth, theme) from feature state (screen-specific), modular feature-based architecture, dependency injection for testability, event-driven communication between features, proper error and loading state handling, state persistence for offline support, and consistent patterns across the team. BLoC or Riverpod with Clean Architecture handles scale well."
        },
        {
            "instruction": "How do you implement advanced testing strategies in Flutter?",
            "input": "",
            "output": "Advanced testing: golden tests (snapshot UI comparison with matchesGoldenFile), property-based testing with fpdart/quickcheck, contract tests for API boundaries, mutation testing to verify test quality, performance tests with benchmarkWidgets, accessibility tests with expectAccessibleNavigation, visual regression tests, and BDD with gherkin. Aim for testing pyramid: many unit, some widget, few integration."
        },
        {
            "instruction": "What are golden tests in Flutter?",
            "input": "",
            "output": "Golden tests capture a rendered widget as a PNG image (golden file) and compare subsequent test runs against it pixel-by-pixel. Create with expectLater(find.byWidget(w), matchesGoldenFile('goldens/my_widget.png')). Update goldens with --update-goldens flag. They catch unintended visual changes. Use with different text scales, themes, and screen sizes for comprehensive visual coverage."
        },
        {
            "instruction": "How do you implement a design system in Flutter?",
            "input": "",
            "output": "A Flutter design system includes: ThemeData/ThemeExtension for colors, typography, spacing tokens, custom widget library (buttons, inputs, cards) with consistent API, documentation with widgetbook or storybook_flutter for visual catalog, automated golden tests for visual regression, a separate package for reuse across projects, and design tokens synced with Figma via code generation."
        },
        {
            "instruction": "How does Flutter's scheduler work?",
            "input": "",
            "output": "SchedulerBinding manages frame callbacks in priority order: 1) transientCallbacks — animation ticks registered via scheduleFrameCallback. 2) persistentCallbacks — registered once for every frame (build/layout/paint pipeline). 3) postFrameCallbacks — run after the frame, for one-time post-paint work via addPostFrameCallback. The scheduler coordinates with the engine's vsync signal to drive the rendering pipeline."
        },
        {
            "instruction": "How do you implement advanced navigation patterns with nested routers?",
            "input": "",
            "output": "Nested routers use separate Navigator widgets for independent navigation stacks. GoRouter supports this with ShellRoute for shared UI (like bottom nav) around child routes. Each tab maintains its own navigation stack. AutoRoute uses AutoTabsRouter for similar functionality. Key challenges: handling system back button, deep linking to nested pages, and state preservation across tabs."
        },
        {
            "instruction": "How do you implement feature flags in Flutter?",
            "input": "",
            "output": "Feature flags control feature visibility without redeployment. Options: Firebase Remote Config for server-controlled flags, LaunchDarkly SDK for advanced targeting, or custom implementation using SharedPreferences/API. Wrap features with if(featureFlags.isEnabled('feature')). Support gradual rollout, A/B testing, and quick disable for broken features. Clean up flags after full rollout."
        },
        {
            "instruction": "How do you implement event-driven architecture in Flutter?",
            "input": "",
            "output": "Event-driven architecture uses an event bus for decoupled communication between features. Implement with: StreamController-based event bus, the event_bus package, or BLoC's event system. Features emit domain events (UserLoggedIn, OrderPlaced) and other features listen. This reduces coupling between modules. EventBus is globally registered, features subscribe in initState and unsubscribe in dispose."
        },
        {
            "instruction": "How does Dart handle concurrency with async/await vs isolates?",
            "input": "",
            "output": "async/await handles I/O-bound concurrency (network calls, file reads) on the single event loop — it doesn't create new threads but yields execution during waits. Isolates handle CPU-bound concurrency (image processing, JSON parsing) by running code in separate memory spaces with dedicated event loops. Use async/await for most tasks; use Isolate.run for computations exceeding 16ms (one frame)."
        },
        {
            "instruction": "How do you implement a micro-frontend architecture in Flutter?",
            "input": "",
            "output": "Micro-frontends in Flutter use modular packages for independent feature development. Each feature is a separate package with its own routes, state, and tests. The main app composes features via dependency injection and route registration. Communication uses an event bus or shared abstractions. This enables independent team development, separate CI/CD, and feature isolation."
        },
        {
            "instruction": "How do you implement crash reporting and analytics in Flutter?",
            "input": "",
            "output": "Crash reporting uses Firebase Crashlytics (FirebaseCrashlytics.instance.recordError) or Sentry (Sentry.captureException). Catch Flutter errors with FlutterError.onError and async errors with PlatformDispatcher.instance.onError. Analytics use Firebase Analytics, Mixpanel, or Amplitude. Track screen views, user actions, and custom events. Tag crashes with user info, device details, and app state for debugging."
        },
        {
            "instruction": "How do you implement app performance monitoring in Flutter?",
            "input": "",
            "output": "Performance monitoring: Firebase Performance Monitoring for network and custom traces, Sentry Performance for transaction tracing, Flutter DevTools for frame rendering analysis. Track custom metrics with Trace API. Monitor: app startup time, HTTP request latency, frame build/raster times, memory usage. Set performance budgets and alert on regressions. Profile with Timeline events."
        },
        {
            "instruction": "How do you implement efficient state management for large lists?",
            "input": "",
            "output": "Large list state management: use ListView.builder for lazy rendering, implement pagination (load by page, not all at once), store items in a Map<String, Item> for O(1) lookup, avoid rebuilding entire list on single item change (use Selector/select), implement virtualization with fixed-height items, cache list state across navigation, and use efficient diffing algorithms for updates."
        },
        {
            "instruction": "How do you implement modular architecture in Flutter?",
            "input": "",
            "output": "Modular architecture organizes code into feature-based packages/folders with clear boundaries. Each module has its own routes, screens, state, models, and repositories. Modules communicate via interfaces/abstract classes, not concrete implementations. A di_module registers dependencies, and a route_module registers routes. This enables independent development, testing, and potential extraction into separate packages."
        },
        {
            "instruction": "How do you implement custom transitions with SharedAxisTransition?",
            "input": "",
            "output": "SharedAxisTransition from the animations package implements Material motion patterns. It transitions between two widgets along a shared axis (horizontal, vertical, or scaled). Use PageTransitionSwitcher with SharedAxisTransitionBuilder. Configure transitionType (SharedAxisTransitionType.horizontal/vertical/scaled). Other Material transitions include FadeThroughTransition, FadeScaleTransition, and OpenContainer for container transform."
        },
        {
            "instruction": "How do you implement code obfuscation in Flutter?",
            "input": "",
            "output": "Code obfuscation renames symbols to prevent reverse engineering. Build with: flutter build apk --obfuscate --split-debug-info=debug_info/. This renames classes, methods, and variables to meaningless names. The debug info directory contains symbol maps for de-obfuscating stack traces. Upload symbol maps to Crashlytics/Sentry for readable crash reports. Obfuscation is production-only and is one layer of app protection."
        },
        {
            "instruction": "How do you implement method channels with Kotlin and Swift?",
            "input": "",
            "output": "Kotlin: In MainActivity, configure FlutterEngine and set MethodCallHandler on MethodChannel. Handle method calls in a when(call.method) block, returning result.success(data) or result.error(). Swift: In AppDelegate, register FlutterMethodChannel on FlutterViewController's binaryMessenger. Handle with channel.setMethodCallHandler { call, result in }. Both use StandardMessageCodec for serialization."
        },
        {
            "instruction": "How do you implement advanced Dart patterns like sealed classes?",
            "input": "",
            "output": "Sealed classes (Dart 3.0) restrict which classes can extend/implement them to the same library. Combined with exhaustive pattern matching: switch(state) { case Loading(): ...; case Success(data: var d): ...; case Error(message: var m): ...; }. The compiler ensures all subtypes are handled. Sealed classes are ideal for state types, result types, and discriminated unions."
        },
        {
            "instruction": "What are Dart patterns and how to use them?",
            "input": "",
            "output": "Dart 3.0 patterns enable destructuring and matching. Types: constant (case 42:), variable (case var x:), typed (case int x:), wildcard (case _:), list ([a, b, ...rest]), map ({'key': value}), record ((x, y: z)), object (MyClass(field: var f)). Use in switch, if-case, for-in, and variable declarations. Patterns are irrefutable (always match) or refutable (may not match)."
        },
        {
            "instruction": "How do you implement Dart records for multiple return values?",
            "input": "",
            "output": "Records (Dart 3.0) are anonymous, immutable, aggregate types: (String, int) coordinate = ('hello', 42). Named fields: ({String name, int age}) person = (name: 'John', age: 30). Access positional fields with .$1, .$2; named fields by name. Records have value equality. They replace the need for Pair/Tuple classes or creating classes just to return multiple values."
        },
        {
            "instruction": "How do you implement class modifiers in Dart 3?",
            "input": "",
            "output": "Dart 3 class modifiers control inheritance: base (extend only, no implement), interface (implement only, no extend), final (no extend or implement outside library), sealed (closed set of subtypes in same library), mixin (can be used as mixin). abstract can combine with any modifier. These enforce API contracts: final class prevents subclassing, sealed enables exhaustive switches."
        },
        {
            "instruction": "How do you implement advanced stream transformations in Dart?",
            "input": "",
            "output": "Advanced stream transformations: transform() with StreamTransformer for custom processing, switchMap (cancel previous, subscribe to new — from RxDart), debounceTime/throttleTime for rate limiting, combineLatest/zip for merging streams, scan for accumulation, distinct for dedup, asyncExpand for async mapping to streams. RxDart provides reactive extensions beyond dart:async Streams."
        },
        {
            "instruction": "How do you implement proper widget decomposition in Flutter?",
            "input": "",
            "output": "Widget decomposition extracts subtrees into custom widgets for readability, reusability, and performance. Guidelines: extract when a subtree exceeds ~100 lines, has its own state, or is reused. Prefer creating StatelessWidget subclasses over helper methods — methods can't have their own build context or keys and don't optimize rebuilds. Pass data via constructor parameters, not InheritedWidgets for local data."
        },
        {
            "instruction": "How do you implement an app-level error handling strategy?",
            "input": "",
            "output": "Comprehensive error handling: 1) FlutterError.onError for framework errors → log and show fallback UI. 2) PlatformDispatcher.instance.onError for uncaught async errors → log and report. 3) runZonedGuarded for zone-level capture. 4) Try-catch in repositories/services with custom exception types. 5) Error states in BLoC/Riverpod. 6) ErrorWidget.builder for custom error display. 7) Global error reporting (Crashlytics/Sentry)."
        },
        {
            "instruction": "How do you implement deferred loading (lazy loading) in Flutter?",
            "input": "",
            "output": "Deferred loading uses Dart's deferred as keyword to load libraries on demand: import 'heavy_feature.dart' deferred as heavy; then await heavy.loadLibrary(); heavy.startFeature(). This reduces initial app size by splitting code into separate JavaScript files (web) or loading code lazily. On mobile, deferred loading reduces initial compilation time."
        },
        {
            "instruction": "How do you implement a complex form with dynamic fields in Flutter?",
            "input": "",
            "output": "Dynamic forms use a Form widget with a list of field definitions (JSON schema or model). Generate FormFields dynamically using ListView.builder based on the schema. Each field has a unique key for state management. Use FormState.save() to collect all values. Handle add/remove fields with setState. Validate with field-specific validators. Use reactive_forms package for complex reactive forms."
        },
        {
            "instruction": "How do you implement proper state machines in Flutter?",
            "input": "",
            "output": "State machines model finite states and valid transitions. In Flutter, implement with BLoC's event→state pattern or dedicated packages like state_machine. Define states (Idle, Loading, Loaded, Error), events (Load, Refresh, Reset), and valid transitions. Invalid transitions are ignored or logged. State machines prevent illegal states, make flows predictable, and simplify debugging complex UI flows."
        },
        {
            "instruction": "How do you implement advanced CustomPainter with complex paths?",
            "input": "",
            "output": "Advanced CustomPainter uses Path for complex shapes: moveTo/lineTo for lines, quadraticBezierTo for quadratic curves, cubicTo for cubic Bezier curves, arcTo for arcs, addPolygon for polygons. Use Path.combine for boolean operations (union, intersect, difference). PathMetric provides path length for animations. Clip with clipPath. Cache Path objects in shouldRepaint() returns false scenarios."
        },
        {
            "instruction": "How do you implement real-time features with Firebase Realtime Database?",
            "input": "",
            "output": "Firebase Realtime Database provides real-time synchronization. Use DatabaseReference for CRUD: ref.set(data), ref.update(data), ref.remove(), ref.get(). Listen with ref.onValue for continuous updates returning DataSnapshot. Structure data flat (avoid deep nesting), use keys for relationships, set security rules. Offline persistence is built-in. For complex queries, prefer Firestore."
        },
        {
            "instruction": "How do you implement the Adapter pattern in Flutter?",
            "input": "",
            "output": "The Adapter pattern converts one interface to another. In Flutter, it is commonly used to convert API response models to domain entities: class UserAdapter { static User fromDto(UserDto dto) => User(name: dto.fullName, email: dto.emailAddress); }. This decouples the domain layer from API contracts. Use adapters in repository implementations to transform data source models."
        },
        {
            "instruction": "How do you implement composable widgets in Flutter?",
            "input": "",
            "output": "Composable widgets are small, focused widgets combined to create complex UIs. Use composition over inheritance — build complex widgets by nesting simple ones. Accept Widget parameters (like leading, trailing, header) for customizable slots. Use typedef for callback signatures. Builder pattern enables widget construction: MyWidget.primary(...), MyWidget.secondary(...). This promotes reusability and consistent API design."
        },
        {
            "instruction": "How do you implement app startup optimization in Flutter?",
            "input": "",
            "output": "Startup optimization: minimize code in main() before runApp, defer non-critical initialization using Future.microtask or addPostFrameCallback, use lazy singletons for services, minimize first-frame widget complexity, implement splash screen for perceived performance, pre-warm image cache, use deferred imports for feature code, enable ahead-of-time compilation, and monitor startup traces in DevTools."
        },
        {
            "instruction": "How do you implement a proper logging system in Flutter?",
            "input": "",
            "output": "Proper logging uses the logger or logging package instead of print(). Define log levels (debug, info, warning, error, fatal). Use Logger class with named loggers per class/module. Configure output format, filters, and destinations (console, file, remote service). In release builds, disable debug/verbose logs. Send error logs to Crashlytics/Sentry. Use structured logging with contextual data."
        },
        {
            "instruction": "How do you implement Canvas-based game rendering in Flutter?",
            "input": "",
            "output": "Canvas-based games use CustomPainter with a game loop driven by Ticker/AnimationController. The game loop updates entity positions (physics), checks collisions, and calls setState to trigger repaint. Use GestureDetector for input, Isolate for physics computation, SpriteSheet rendering with drawImageRect. For complex games, use the Flame engine which provides a component system, collision detection, and sprite animations."
        },
        {
            "instruction": "What is the Flame game engine for Flutter?",
            "input": "",
            "output": "Flame is a 2D game engine built on Flutter. It provides: FlameGame (main game loop with update/render), Component system (composable game objects), SpriteComponent/SpriteAnimationComponent (rendering), collision detection, input handling (tap, drag, keyboard), effects system for animations, camera and viewport, tile maps, and particle systems. It integrates with Flutter widgets via GameWidget."
        },
        {
            "instruction": "How do you implement proper dependency management in Flutter?",
            "input": "",
            "output": "Dependency management: pin exact versions in pubspec.yaml with = or narrow ranges, use pubspec.lock for reproducible builds, run 'dart pub outdated' to check for updates, 'dart pub upgrade --major-versions' for major updates. Prefer well-maintained packages (pub.dev points, null safety). Minimize dependencies to reduce attack surface and build size. Version conflicts use dependency_overrides cautiously."
        },
        {
            "instruction": "How do you implement token-based authentication flow in Flutter?",
            "input": "",
            "output": "Token auth flow: 1) Login sends credentials to API, receives access_token and refresh_token. 2) Store tokens securely with flutter_secure_storage. 3) Attach access_token to requests via Dio interceptor (Authorization: Bearer token). 4) On 401 response, use refresh_token to get new access_token. 5) On refresh failure, redirect to login. Handle token expiration, concurrent refresh requests, and secure storage migration."
        },
        {
            "instruction": "How do you implement advanced image processing in Flutter?",
            "input": "",
            "output": "Advanced image processing uses the image package for manipulation (resize, crop, rotate, filter, format conversion) on isolates to avoid jank. For real-time processing, use camera package with isolate-based frame processing. ML-based processing uses google_mlkit_image_labeling, tflite_flutter for custom models. Canvas-based processing applies filters via ColorFilter, ShaderMask, and custom shaders."
        },
        {
            "instruction": "How do you implement app architecture documentation in Flutter?",
            "input": "",
            "output": "Architecture documentation includes: README with architecture overview, module dependency diagram, data flow diagrams for key features, state management conventions, naming conventions, folder structure rationale, API integration patterns, error handling strategy, testing strategy, and code review checklist. Use Mermaid diagrams in Markdown. Maintain architecture decision records (ADRs) for significant choices."
        },
        {
            "instruction": "How does BuildContext work and what are its limitations?",
            "input": "",
            "output": "BuildContext is a handle to the widget's location in the widget tree, actually an Element reference. It is used to find ancestors (Theme.of, Navigator.of, Provider.of). Limitations: context is only valid during and after build(), not in initState() without addPostFrameCallback. It reflects the current tree position — moving a widget changes its context. Don't store contexts or use them across async gaps."
        },
        {
            "instruction": "How do you implement proper async initialization patterns in Flutter?",
            "input": "",
            "output": "Async initialization patterns: 1) FutureBuilder in widget tree for async data loading. 2) WidgetsBinding.instance.addPostFrameCallback in initState for post-build async work. 3) Provider's create: (_) async => await init() for service initialization. 4) GetIt's signalsReady/allReady for dependent service initialization. 5) Custom splash screen waiting for initialization Futures to complete."
        },
        # ─── More Advanced Questions (Batch 2) ─────────────────────────────────
        {
            "instruction": "How does Flutter's widget reconciliation algorithm work?",
            "input": "",
            "output": "Flutter's reconciliation (diffing) algorithm compares old and new widget trees element-by-element. It uses widget runtimeType and key to match elements. If type matches, the element is updated (updateChild). If type differs, the old element is deactivated and a new one is inflated. Keys force identity-based matching within lists. The algorithm is O(n) for lists with keys, handling reorders, insertions, and deletions efficiently. Without keys, it uses positional matching which can cause incorrect state preservation."
        },
        {
            "instruction": "How does the Flutter engine handle frame scheduling and vsync?",
            "input": "",
            "output": "The Flutter engine uses SchedulerBinding to coordinate frame callbacks with the display vsync signal. When setState is called, the framework schedules a frame via SchedulerBinding.scheduleFrame(). On vsync, the engine calls beginFrame triggering transientCallbacks (animations), then drawFrame triggering persistentCallbacks (build/layout/paint). If a frame exceeds 16ms (60fps), jank occurs. SchedulerBinding.addTimingsCallback monitors frame timing. The engine pipelines frames, starting the next while the GPU composites the current one."
        },
        {
            "instruction": "How do you implement a custom layout algorithm in Flutter?",
            "input": "",
            "output": "Custom layouts override MultiChildRenderObjectWidget with a custom RenderBox. Override performLayout to position children: iterate children via firstChild/childAfter, call child.layout(constraints, parentUsesSize: true) to size each child, then set child's parentData offset for positioning. Override setupParentData to use custom ParentData for storing position info. Override paint to paint children at their offsets. This enables layouts like circular arrangements, masonry grids, or custom flow algorithms."
        },
        {
            "instruction": "How does Dart's garbage collector work and impact Flutter performance?",
            "input": "",
            "output": "Dart uses a generational garbage collector with young and old spaces. Young space uses semi-space copying — frequent, fast collections for short-lived objects. Old space uses mark-sweep-compact for long-lived objects. GC runs on the main isolate, potentially causing frame drops during old-space collection. Minimize GC pressure by: reusing objects, avoiding excessive allocations in build(), using const constructors, pooling frequently created objects. Profile GC with DevTools timeline. Isolates have independent heaps, so compute-heavy work in isolates avoids main isolate GC pauses."
        },
        {
            "instruction": "How do you implement a custom render object with hit testing?",
            "input": "",
            "output": "Custom hit testing overrides hitTestSelf and hitTestChildren in RenderBox. hitTestSelf returns true if the point is within the render object's bounds. hitTestChildren iterates children in reverse paint order (last painted = first hit tested). Use BoxHitTestResult.addWithPaintOffset to transform coordinates for children. For custom shapes, override hitTestSelf with path.contains(position). The hit test traverses the render tree from root, building a HitTestResult path to the deepest widget that accepts the hit."
        },
        {
            "instruction": "How does Flutter handle platform thread architecture?",
            "input": "",
            "output": "Flutter uses four thread (task runner) types: UI thread runs Dart code (framework, build, layout, paint), Raster thread composites layers and submits to GPU, Platform thread handles platform messages and plugin code, IO thread handles expensive IO operations (image decoding, asset loading). Blocking the UI thread causes jank. Blocking the raster thread causes frame drops. Platform channels run on the platform thread by default. Isolates create additional threads for compute-heavy work."
        },
        {
            "instruction": "How do you implement custom shader effects in Flutter?",
            "input": "",
            "output": "Custom shaders use FragmentProgram API. Write GLSL fragment shaders (.frag files), compile with flutter build. Load: final program = await FragmentProgram.fromAsset('shaders/effect.frag'). Create shader: final shader = program.fragmentShader()..setFloat(0, time)..setImageSampler(0, image). Apply with CustomPainter using Paint()..shader = shader. Shaders enable effects like blur, distortion, color manipulation, and procedural textures. Works with Impeller and Skia backends."
        },
        {
            "instruction": "How does Flutter's layer tree and compositing work?",
            "input": "",
            "output": "After paint, Flutter creates a layer tree (Scene) that maps to GPU operations. Key layers: OffsetLayer (positioning), OpacityLayer (alpha), ClipRectLayer (clipping), TransformLayer (transforms), PictureLayer (draw commands), TextureLayer (platform textures). RepaintBoundary creates a separate OffsetLayer, enabling partial repaint. The raster thread composites layers, caching unchanged layers. Too many layers increase GPU memory and compositing cost. Profile with DevTools Layers tab. Impeller pre-compiles shaders, eliminating shader compilation jank."
        },
        {
            "instruction": "How do you implement effective state management at scale with BLoC?",
            "input": "",
            "output": "BLoC at scale: 1) One BLoC per feature, not per screen. 2) Use sealed Events with Freezed for exhaustive handling. 3) Use sealed States with explicit loading/success/error substates. 4) Inject repositories via constructor for testability. 5) Use BlocObserver for centralized logging/analytics. 6) Avoid BLoC-in-BLoC dependencies — use repository layer for shared data. 7) Use emit.forEach for stream subscriptions. 8) Handle concurrent events with transformers (sequential, droppable, restartable). 9) Unit test every event→state transition."
        },
        {
            "instruction": "How do you implement advanced isolate communication patterns?",
            "input": "",
            "output": "Advanced isolate patterns beyond compute(): 1) Long-lived worker isolates with bidirectional SendPort/ReceivePort communication. 2) Isolate groups (Isolate.spawn) share heap for faster message passing. 3) TransferableTypedData for zero-copy large data transfer. 4) Multiple worker pool pattern with load balancing. 5) Shared memory via typed data views in Dart 3. 6) Error handling with Isolate.errors stream. 7) Graceful shutdown with kill/pause capabilities. For complex patterns, use the worker_manager or squadron packages."
        },
        {
            "instruction": "How do you implement deep link handling with universal links and app links?",
            "input": "",
            "output": "Universal links (iOS) require apple-app-site-association file on your domain, Associated Domains entitlement in Xcode. App Links (Android) require assetlinks.json on your domain, intent-filter with autoVerify in AndroidManifest. In Flutter, use app_links package: AppLinks().uriLinkStream.listen((uri) { router.go(uri.path); }). Handle initial link: AppLinks().getInitialLink(). Configure GoRouter with redirect logic for deep link paths. Test with adb shell am start and xcrun simctl openurl."
        },
        {
            "instruction": "How do you implement custom scrolling physics in Flutter?",
            "input": "",
            "output": "Custom physics extend ScrollPhysics, overriding applyPhysicsToUserOffset (drag behavior), applyBoundaryConditions (over-scroll), createBallisticSimulation (fling/settle behavior). Example: snapping physics that settle to nearest item: override createBallisticSimulation to return ScrollSpringSimulation targeting the nearest snap point. Override shouldAcceptUserOffset for custom drag acceptance. Chain physics with parent parameter. Use FixedExtentScrollPhysics as reference for snap-to-item behavior."
        },
        {
            "instruction": "How does tree shaking work in Flutter and Dart?",
            "input": "",
            "output": "Tree shaking eliminates unused code during compilation. Dart's AOT compiler performs whole-program analysis, identifying reachable code from main(). Unreachable classes, methods, and functions are excluded from the binary. However, dart:mirrors (reflection) prevents tree shaking since all code is potentially reachable. Build_runner codegen enables tree-shaking-friendly alternatives to reflection. Icons.material_icons uses tree shaking with --tree-shake-icons flag. Conditional imports allow platform-specific tree shaking."
        },
        {
            "instruction": "How do you implement advanced testing strategies for Flutter apps?",
            "input": "",
            "output": "Advanced testing: 1) Golden tests verify pixel-perfect rendering: expectLater(find.byType(Widget), matchesGoldenFile('golden.png')). 2) Integration tests with patrol_cli for native interactions. 3) BLoC testing with blocTest() for event→state sequences. 4) Mutation testing with mutation_test to verify test quality. 5) Property-based testing with glados for generative test cases. 6) Accessibility testing with checkSemanticsLabel and semantics matchers. 7) Performance testing with traceAction in integration tests. 8) Screenshot testing across multiple devices."
        },
        {
            "instruction": "How does Flutter's Impeller rendering engine differ from Skia?",
            "input": "",
            "output": "Impeller pre-compiles all shaders during build time, eliminating runtime shader compilation jank that plagued Skia. Impeller uses Metal on iOS and Vulkan/OpenGL on Android. It employs a tessellation-based approach instead of Skia's stencil-then-cover. Impeller's architecture is optimized for mobile GPUs with batched draw calls. Runtime performance is more predictable. Impeller enabled by default on iOS (Flutter 3.16+). On Android, it's being stabilized. Custom shaders work with both engines but may need adaptation."
        },
        {
            "instruction": "How do you implement a custom InheritedWidget with update notification?",
            "input": "",
            "output": "Custom InheritedWidget: class MyInherited extends InheritedWidget { final int data; const MyInherited({required this.data, required super.child}); static MyInherited of(BuildContext context) => context.dependOnInheritedWidgetOfExactType<MyInherited>()!; @override bool updateShouldNotify(MyInherited old) => data != old.data; }. Wrap with StatefulWidget to update data. updateShouldNotify controls rebuild propagation — return true only when dependents need to rebuild. For finer control, use InheritedModel with aspects for partial dependency."
        },
        {
            "instruction": "How do you implement advanced CI/CD pipelines for Flutter?",
            "input": "",
            "output": "Advanced CI/CD: GitHub Actions/Codemagic/Bitrise workflows include: 1) Matrix builds testing multiple Flutter versions. 2) Code quality gates: analyze, format check, coverage thresholds. 3) Golden test comparison with tolerance. 4) Integration tests on Firebase Test Lab. 5) Automated versioning with semantic_release. 6) Build flavors/environments (dev/staging/prod). 7) Code signing automation with match (iOS) and keystore management (Android). 8) Automated store deployment with fastlane. 9) Slack/Teams notifications. 10) Artifact caching for faster builds."
        },
        {
            "instruction": "How do you implement a custom painting pipeline for complex visualizations?",
            "input": "",
            "output": "Complex visualizations layer multiple CustomPainters or use a single painter with structured drawing phases. Use Canvas operations: drawPath for lines/shapes, drawArc for arcs, drawCircle, drawRect, drawPoints. Apply Paint with shader (LinearGradient, RadialGradient), blendMode, maskFilter (blur), colorFilter. Optimize with shouldRepaint checking data changes. Use RepaintBoundary for isolated repaints. For large datasets, pre-compute paths and cache. TextPainter renders text at specific positions."
        },
        {
            "instruction": "How do you implement secure API communication in Flutter?",
            "input": "",
            "output": "Secure API communication: 1) Use HTTPS exclusively. 2) Certificate pinning with SecurityContext or dio_http2_adapter. 3) API key rotation — never hardcode keys, use --dart-define or .env. 4) JWT with refresh token rotation — store in flutter_secure_storage. 5) Request signing (HMAC) for API integrity. 6) CORS handling for web. 7) Rate limiting awareness with retry-after headers. 8) Input sanitization before sending. 9) Response validation against expected schemas. 10) Obfuscate with --obfuscate --split-debug-info for release builds."
        },
        {
            "instruction": "How do you implement complex animation orchestration in Flutter?",
            "input": "",
            "output": "Complex orchestration: 1) Staggered animations with Interval curves on a single AnimationController: slideAnim = Tween<Offset>(...).animate(CurvedAnimation(parent: controller, curve: Interval(0.0, 0.5, curve: Curves.easeOut))). 2) AnimationController chaining with StatusListener — start next animation when previous completes. 3) TweenSequence for multi-phase animations on one controller. 4) Rive/Lottie for design-tool animations. 5) Custom TweenAnimationBuilder compositions for declarative complex animations."
        },
        {
            "instruction": "How do you implement memory leak detection and prevention in Flutter?",
            "input": "",
            "output": "Memory leak prevention: 1) Always dispose controllers (AnimationController, TextEditingController, ScrollController) in dispose(). 2) Cancel StreamSubscriptions and Timers. 3) Remove listeners added with addListener. 4) Use DevTools Memory tab to capture heap snapshots and track allocations. 5) LeakTracker in tests catches common leaks. 6) Avoid closures capturing BuildContext across async gaps. 7) Use weak references for caches. 8) Profile with --profile mode. 9) Watch for retained elements after navigation."
        },
        {
            "instruction": "How does Flutter handle text rendering and layout internally?",
            "input": "",
            "output": "Flutter's text rendering pipeline: RenderParagraph → TextPainter → Paragraph (engine). TextPainter creates a ui.Paragraph from TextSpan, handling rich text with multiple styles. The engine uses HarfBuzz for text shaping (ligatures, kerning), ICU for line breaking and bidi. Layout computes line breaks, glyph positions, and text metrics. Paint draws glyphs via Skia/Impeller. Custom text layout with TextPainter.layout(minWidth, maxWidth) computes metrics before painting."
        },
        {
            "instruction": "How do you implement feature flags in Flutter apps?",
            "input": "",
            "output": "Feature flags enable/disable features without deploying. Options: 1) Firebase Remote Config — fetch flags at startup, cache locally, A/B test. 2) LaunchDarkly, Unleash, or Flagsmith SDKs for full-featured solutions. 3) Custom implementation: store flags in API/Firestore, cache locally, check with if (featureFlags.isEnabled('newUI')). Wrap features with conditional widgets. Use compile-time flags with --dart-define for build-time feature toggling. Reset cached flags periodically."
        },
        {
            "instruction": "How do you implement add-to-app (embedding Flutter in existing native apps)?",
            "input": "",
            "output": "Add-to-app embeds Flutter as a module in existing iOS/Android apps. Create Flutter module with flutter create --template module. iOS: add to Podfile as pod 'Flutter'. Android: add as dependency in settings.gradle. Use FlutterEngine for warm-up, FlutterViewController (iOS) or FlutterActivity (Android) to display Flutter. Share data via MethodChannel. Multiple Flutter engines supported but memory-expensive. Pre-warm engine in Application.onCreate for faster launch."
        },
        {
            "instruction": "How do you optimize Flutter app startup time?",
            "input": "",
            "output": "Startup optimization: 1) Defer heavy initialization with lazy loading. 2) Reduce main() work — move initialization after first frame. 3) Use deferred components (--deferred-components) for download-on-demand. 4) Minimize import graph breadth — tree shaking is limited by imports. 5) Pre-warm FlutterEngine. 6) Use native splash to cover init time. 7) Reduce asset bundle size. 8) Profile startup with flutter run --trace-startup. 9) Use Isolate.run for CPU-heavy init. 10) AOT compilation (release mode) is significantly faster than JIT."
        },
        {
            "instruction": "How do you implement custom semantics for accessibility in Flutter?",
            "input": "",
            "output": "Custom semantics use Semantics widget: Semantics(label: 'Play button', hint: 'Double tap to play video', value: '0:30', onTap: play, child: customWidget). For complex widgets, use MergeSemantics, ExcludeSemantics, BlockSemantics to control the semantics tree. Custom render objects override describeSemanticsConfiguration. Test with SemanticsHandle in widget tests. Validate with Accessibility Inspector (iOS) and TalkBack (Android). Follow WCAG guidelines."
        },
        {
            "instruction": "How do you implement Dart 3 sealed classes for state management?",
            "input": "",
            "output": "Dart 3 sealed classes enable exhaustive pattern matching for states: sealed class AuthState {} class Authenticated extends AuthState { final User user; Authenticated(this.user); } class Unauthenticated extends AuthState {} class Loading extends AuthState {}. Use switch expression for exhaustive handling: switch (state) { case Authenticated(:final user) => HomeScreen(user), case Unauthenticated() => LoginScreen(), case Loading() => LoadingScreen() }. Compiler ensures all cases are handled. Combined with BLoC or Riverpod, this provides type-safe state transitions."
        },
        {
            "instruction": "How do you implement advanced Dart patterns and destructuring?",
            "input": "",
            "output": "Dart 3 patterns enable destructuring and matching: 1) Record patterns: var (x, y) = getPoint(). 2) Object patterns: case User(name: String n, age: >= 18) => 'Adult: $n'. 3) List patterns: case [first, ...rest] => process(first, rest). 4) Map patterns: case {'name': String name} => name. 5) Guard clauses: case int x when x > 0 => 'positive'. 6) Logical patterns: case >= 0 && <= 100 => 'percentage'. 7) Null-check patterns: case var value? => 'non-null'. Used in switch expressions, if-case, and variable declarations."
        },
        {
            "instruction": "How do you implement platform views in Flutter?",
            "input": "",
            "output": "Platform views embed native UI (UIKit/Android Views) in Flutter. Android: extend PlatformView, register with PlatformViewFactory. Use AndroidView widget with viewType. Hybrid Composition (default) renders natively for best compatibility. Virtual Display renders to a texture for better performance but has limitations. iOS: use UiKitView with UIPlatformView. Platform views are expensive — each adds a native view layer. Minimize usage and prefer Flutter widgets when possible."
        },
        {
            "instruction": "How do you implement complex form validation architecture?",
            "input": "",
            "output": "Complex form architecture: 1) FormBloc/FormNotifier per form separating validation from UI. 2) Field-level validators composed: email = required.then(emailFormat).then(unique). 3) Cross-field validation: passwordConfirm depends on password field. 4) Async validation with debouncing: check username availability. 5) Validation on change, on blur, or on submit modes. 6) Touched/dirty/pristine field states for UX. 7) Form-level computed validity state. 8) Preserve form state across navigation. reactive_forms package implements many of these patterns."
        },
        {
            "instruction": "How do you implement custom sliver layouts in Flutter?",
            "input": "",
            "output": "Custom slivers extend RenderSliver. Override performLayout: receive SliverConstraints (scrollOffset, remainingPaintExtent, crossAxisExtent), compute SliverGeometry (scrollExtent, paintExtent, layoutExtent, maxPaintExtent). Position children relative to scroll offset. Paint override handles scroll-aware rendering. Example: SliverPersistentHeader uses remaining space to shrink/grow. Custom slivers can implement sticky behavior, overlap effects, or dynamic sizing. Use SliverMultiBoxAdaptorWidget for list-like slivers with child management."
        },
        {
            "instruction": "How do you implement app obfuscation and tamper detection?",
            "input": "",
            "output": "Obfuscation: flutter build apk --obfuscate --split-debug-info=debug-info/. This renames classes/methods to meaningless strings. Save debug-info for crash symbolication. Tamper detection: 1) Verify app signature at runtime against known hash. 2) Check for root/jailbreak with flutter_jailbreak_detection. 3) Detect debugger attachment with assertions. 4) Integrity checks on critical binary sections. 5) Certificate pinning detects MITM. 6) Avoid storing secrets in Dart code — use platform keystore. ProGuard/R8 rules protect Android native code."
        },
        {
            "instruction": "How do you implement Flutter web performance optimization?",
            "input": "",
            "output": "Flutter web optimization: 1) Use CanvasKit renderer for complex graphics, HTML renderer for text-heavy apps (--web-renderer canvaskit|html|auto). 2) Enable deferred loading for routes: deferred as lib. 3) Compress assets and use WebP images. 4) Implement code splitting with deferred imports. 5) Use flutter build web --release for optimization. 6) Service worker for offline caching. 7) Avoid Platform.isAndroid checks — use kIsWeb. 8) Minimize custom painting which is expensive on web. 9) Use tree shaking for icon fonts. 10) CDN for static assets."
        },
        {
            "instruction": "How do you implement a plugin that works across all Flutter platforms?",
            "input": "",
            "output": "Cross-platform plugins use federated plugin architecture. Create interface package (plugin_platform_interface) with method signatures. Create platform-specific implementations: plugin_android with MethodChannel, plugin_ios with MethodChannel, plugin_web with dart:js_interop, plugin_windows/linux/macos with dart:ffi. The app-facing package (plugin) provides the public API. Each platform registers its implementation with PlatformInterface. This allows independent platform development and third-party platform additions."
        },
        {
            "instruction": "How do you implement efficient list rendering for large datasets?",
            "input": "",
            "output": "Efficient large lists: 1) ListView.builder for lazy item creation — only builds visible items plus pre-cache extent. 2) Use const widgets for static items. 3) Cache item heights with AutomaticKeepAliveClientMixin for consistent scrolling. 4) Use RepaintBoundary per item for isolated repaints. 5) Avoid expensive computations in itemBuilder — precompute data. 6) Use CacheExtent to control how many items are pre-rendered. 7) For heterogeneous items, prefer SliverList over ListView. 8) Implement proper keys for stateful items. 9) Use indexed_list_view for massive lists."
        },
        {
            "instruction": "How do you implement advanced error boundaries in Flutter?",
            "input": "",
            "output": "Error boundaries prevent error propagation through widget tree. Implement: class ErrorBoundary extends StatefulWidget { Widget build() { return ErrorWidget.builder = (details) => ErrorFallback(details); } }. Override FlutterError.onError for framework errors. Use runZonedGuarded for uncaught async errors. PlatformDispatcher.instance.onError for platform errors. Create context-aware error boundaries that show relevant fallback UI. Log errors to Crashlytics/Sentry. In debug mode, show detailed error info."
        },
        {
            "instruction": "How do you implement Dart FFI for native library integration?",
            "input": "",
            "output": "Dart FFI (dart:ffi) calls C/C++ native functions directly. Define function signatures: typedef NativeAdd = Int32 Function(Int32, Int32). Load library: final lib = DynamicLibrary.open('libnative.so'). Lookup function: final add = lib.lookupFunction<NativeAdd, DartAdd>('add'). For structs: extend Struct with @Array annotations. Use Pointer<T> for memory management. ffigen auto-generates Dart bindings from C headers. Allocate/free memory with calloc/malloc. Always free native memory to prevent leaks."
        },
        {
            "instruction": "How do you implement performance profiling in Flutter production apps?",
            "input": "",
            "output": "Production profiling: 1) Firebase Performance Monitoring — automatic HTTP metrics, custom traces with trace.start()/stop(), metrics with trace.setMetric('frames', count). 2) Sentry Performance for distributed tracing. 3) Custom PerformanceOverlay in hidden debug menu. 4) SchedulerBinding.addTimingsCallback for frame timing in production. 5) Timeline events with dart:developer Timeline.startSync. 6) App size analysis with --analyze-size flag. 7) Startup trace with --trace-startup. 8) Memory profiling in profile mode."
        },
        {
            "instruction": "How do you implement state restoration in Flutter?",
            "input": "",
            "output": "State restoration preserves UI state across process death. Enable with RestorationMixin on State class. Register restorable properties: final RestorableInt _counter = RestorableInt(0); Override restoreState: registerForRestoration(_counter, 'counter'). Use RestorableTextEditingController for text fields. Set restorationId on MaterialApp and navigators. Restorable scroll positions with restorationId on ScrollView. Override restorationId getter. State is serialized to platform's state restoration mechanism."
        },
        {
            "instruction": "How do you implement advanced dependency injection in Flutter?",
            "input": "",
            "output": "Advanced DI patterns: 1) GetIt service locator with lazy/eager singletons, factories, and async registration. 2) Injectable code generation for automatic GetIt registration. 3) Scoped registration with pushNewScope for per-feature dependencies. 4) Riverpod's ProviderScope overrides for testing and scoping. 5) Multi-layer: interface → implementation → registration. 6) Module-based registration: each feature module registers its dependencies. 7) Environment-based registration: mock vs real implementations. 8) Dispose registered instances with GetIt.reset()."
        },
        {
            "instruction": "How do you implement efficient image loading and caching strategies?",
            "input": "",
            "output": "Image optimization: 1) CachedNetworkImage with placeholder and error widgets — uses sqflite-based disk cache. 2) ResizeImage for memory-efficient loading at display size: Image(image: ResizeImage(NetworkImage(url), width: 200)). 3) precacheImage for pre-loading critical images. 4) FadeInImage for smooth placeholder-to-image transition. 5) Image.memory for decoded bytes. 6) PaintingBinding.instance.imageCache.maximumSize for cache size control. 7) LQIP (Low Quality Image Placeholder) pattern. 8) WebP format for smaller files."
        },
        {
            "instruction": "How do you implement complex navigation patterns with nested routers?",
            "input": "",
            "output": "Nested routing with GoRouter: use ShellRoute for shared UI (bottom nav, sidebar). Each tab maintains its own navigation stack with StatefulShellRoute.indexedStack. Configure branches with StatefulShellBranch, each containing its route tree. NavigatorState per branch preserves scroll position and state. Deep linking maps directly to nested routes. Handle back button behavior per platform. For complex flows, use guard redirects and path parameters across nested routes."
        },
        {
            "instruction": "How do you implement real-time collaboration features in Flutter?",
            "input": "",
            "output": "Real-time collaboration: 1) WebSocket for bidirectional real-time data. 2) Firestore real-time listeners for document synchronization. 3) Operational Transform (OT) or CRDT for conflict-free concurrent editing. 4) Presence indicators using Firestore's onDisconnect or custom heartbeat. 5) Cursor/selection sharing for collaborative editing. 6) Optimistic updates with server reconciliation. 7) Event sourcing for audit trail. 8) Socket.io for room-based collaboration. 9) Yjs/Automerge for CRDT-based data structures."
        },
        {
            "instruction": "How do you implement custom transition animations between routes?",
            "input": "",
            "output": "Custom route transitions use PageRouteBuilder: PageRouteBuilder(pageBuilder: (_, __, ___) => TargetPage(), transitionsBuilder: (_, animation, secondaryAnimation, child) { return SlideTransition(position: Tween<Offset>(begin: Offset(1, 0), end: Offset.zero).animate(CurvedAnimation(parent: animation, curve: Curves.easeInOut)), child: child); }). Secondary animation handles the outgoing route. Combine multiple tween animations for complex effects. Use AnimatedSwitcher for in-page transitions."
        },
        {
            "instruction": "How do you implement micro-frontend architecture in Flutter?",
            "input": "",
            "output": "Micro-frontends in Flutter: 1) Separate Dart packages per feature module with clear API boundaries. 2) Shared core package for common models, themes, and utilities. 3) Dependency injection at module boundaries with abstract interfaces. 4) Each module owns its routes, state, and UI. 5) Module-level routing with nested GoRouter. 6) Mono-repo with Melos for multi-package management. 7) Lazy loading modules with deferred imports. 8) Module communication via events/streams, not direct dependencies. 9) Independent testing per module."
        },
        {
            "instruction": "How do you implement accessibility testing in Flutter?",
            "input": "",
            "output": "Accessibility testing: 1) Widget tests with semantics finders: find.bySemanticsLabel('Submit'). 2) expectSemanticsTree matcher for tree structure. 3) SemanticsHandle for testing semantics actions: handle.performAction(SemanticsAction.tap). 4) guideline checks: expect(tester, meetsGuideline(textContrastGuideline)). 5) Manual testing with TalkBack (Android), VoiceOver (iOS). 6) Accessibility Inspector in Xcode. 7) flutter analyze for missing semantics warnings. 8) Test touch target sizes (minimum 48x48). 9) Test with increased text scale factor."
        },
        {
            "instruction": "How do you implement code push / hot updates without app store releases?",
            "input": "",
            "output": "Code push for Flutter: 1) Shorebird.dev provides code push — patches Dart code without app store review. Integrates with CI/CD. Only patches Dart code, not native code or assets. 2) Firebase Remote Config for feature flags and configuration changes. 3) Server-driven UI — render UI from server JSON definitions. 4) Dynamic module loading with deferred components. Note: Apple and Google restrict executable code download; Shorebird works within platform guidelines. Always plan store releases for native changes."
        },
        {
            "instruction": "How do you implement event-driven architecture in Flutter?",
            "input": "",
            "output": "Event-driven architecture: 1) Event bus with StreamController<Event>.broadcast() for app-wide events. 2) Domain events emitted from repositories/services — UI reacts to domain changes. 3) BLoC pattern is inherently event-driven: Events in, States out. 4) Dart streams for reactive pipelines: transform, where, map, switchMap. 5) CQRS-style: separate command/query models. 6) EventSourcing: store events, reconstruct state. 7) Mediator pattern for decoupled component communication. Use event_bus package for simple pub/sub."
        },
        {
            "instruction": "How do you implement advanced theming with ThemeExtension?",
            "input": "",
            "output": "ThemeExtension adds custom theme properties: class AppColors extends ThemeExtension<AppColors> { final Color success; final Color warning; AppColors({required this.success, required this.warning}); @override ThemeExtension<AppColors> copyWith({Color? success, Color? warning}) => AppColors(success: success ?? this.success, warning: warning ?? this.warning); @override ThemeExtension<AppColors> lerp(covariant AppColors? other, double t) => AppColors(success: Color.lerp(success, other?.success, t)!, warning: Color.lerp(warning, other?.warning, t)!); }. Register: ThemeData(extensions: [AppColors(success: Colors.green, warning: Colors.orange)]). Access: Theme.of(context).extension<AppColors>()!.success."
        },
        {
            "instruction": "How do you implement background geofencing in Flutter?",
            "input": "",
            "output": "Background geofencing uses geofencing_flutter or platform channels. Define geofences with center point, radius, and triggers (enter/exit/dwell). Register with GeofencingClient. Handle events in background with top-level callback functions. On Android, uses Google Play Services Geofencing API. On iOS, uses CLCircularRegion with Core Location. Battery optimization and permissions required. Test with mock locations. Combine with background_fetch for periodic location checks."
        },
        {
            "instruction": "How do you implement a design system in Flutter?",
            "input": "",
            "output": "Design system implementation: 1) Token layer: define color, typography, spacing, radius tokens as constants or ThemeExtension. 2) Primitive components: buttons, inputs, cards extending Flutter widgets with design constraints. 3) Composite components: search bars, list items combining primitives. 4) Documentation with Widgetbook or Storybook for component catalog. 5) Separate package for reuse across apps. 6) Theming support for light/dark/brand variants. 7) Motion tokens for consistent animations. 8) Golden tests for visual regression. 9) Accessibility built into every component."
        },
        {
            "instruction": "How do you implement server-driven UI in Flutter?",
            "input": "",
            "output": "Server-driven UI renders widgets from server JSON definitions. Backend sends UI schema: {\"type\": \"Column\", \"children\": [{\"type\": \"Text\", \"text\": \"Hello\"}]}. Client maps type strings to widget builders: Map<String, WidgetBuilder> registry = {'Text': (json) => Text(json['text']), 'Column': (json) => Column(children: json['children'].map(buildWidget))}. Benefits: update UI without app releases. Challenges: limited interactivity, testing complexity, performance overhead. Use for content-heavy screens, banners, and experiment."
        },
        {
            "instruction": "How do you implement advanced clean architecture in Flutter?",
            "input": "",
            "output": "Clean Architecture layers: 1) Domain: entities (plain Dart classes), use cases (single-responsibility business logic), repository interfaces. 2) Data: repository implementations, data sources (remote/local), models (with toEntity/fromEntity), mappers. 3) Presentation: BLoC/Cubit per feature, pages, widgets. Dependencies point inward: presentation → domain ← data. Use cases encapsulate business rules: class GetUsers { final UserRepository repo; Future<List<User>> call() => repo.getUsers(); }. DI wires layers. Each layer independently testable."
        },
        {
            "instruction": "How do you implement Dart metaprogramming with macros (Dart 3.x)?",
            "input": "",
            "output": "Dart macros (experimental) enable compile-time code generation. Annotate classes with macro annotations: @DataClass() class User { final String name; final int age; }. The macro generates equals, hashCode, toString, copyWith at compile time. Unlike build_runner, macros run during compilation with IDE support. Types: expression macros, declaration macros, type macros. Macros introspect existing code with declaration mirrors and augment with new declarations. Will eventually replace many codegen packages like freezed and json_serializable."
        },
        {
            "instruction": "How do you implement Flutter app size optimization?",
            "input": "",
            "output": "App size optimization: 1) flutter build --analyze-size generates size breakdown. 2) --split-debug-info separates debug symbols. 3) --tree-shake-icons removes unused icon glyphs. 4) Use ProGuard/R8 for Android native code shrinking. 5) Deferred loading splits code into downloadable units. 6) Compress images, use WebP, remove unused assets. 7) Audit dependencies — remove unused packages. 8) Use --split-per-abi for per-architecture APKs (reduces ~50%). 9) Android App Bundle for Play Store delivery optimization. 10) Profile dependencies with dart pub deps."
        },
        # --- Additional Advanced Questions ---
        # Performance Optimization Deep Dives
        {
            "instruction": "How do you profile and fix rendering performance issues in Flutter?",
            "input": "",
            "output": "Profiling workflow: 1) Run in profile mode: flutter run --profile. 2) Open DevTools Performance view — look for red frames (>16ms). 3) Check build phase: if expensive, extract constant widgets, use const constructors, minimize rebuild scope with Consumer/Selector. 4) Check paint phase: if expensive, use RepaintBoundary to isolate regions. 5) Check compositing: reduce opacity, clip, and shader usage. 6) Timeline view shows build/layout/paint/composite per frame. 7) debugProfileBuildsEnabled = true logs build times. 8) Use PerformanceOverlay.allEnabled() to show GPU/UI graphs."
        },
        {
            "instruction": "How do you implement efficient image caching in Flutter?",
            "input": "",
            "output": "Approaches: 1) Default ImageCache: automatically caches ~100MB decoded images. Tune: PaintingBinding.instance.imageCache.maximumSize = 200; PaintingBinding.instance.imageCache.maximumSizeBytes = 500 << 20;. 2) cached_network_image: CachedNetworkImage(imageUrl: url, cacheManager: CacheManager(Config('custom', stalePeriod: Duration(days: 7), maxNrOfCacheObjects: 100)));. 3) extended_image for advanced caching with memory+disk. 4) precacheImage() preloads during splash. 5) ResizeImage(image, width: 200) for memory-efficient thumbnails."
        },
        {
            "instruction": "How do you implement memory leak detection in Flutter?",
            "input": "",
            "output": "Memory leak detection: 1) DevTools Memory tab: take heap snapshots, compare allocations, identify retained objects. 2) Common leaks: un-cancelled StreamSubscriptions, un-disposed AnimationControllers, un-removed listeners, closures capturing BuildContext. 3) leak_tracker package for automated detection. 4) Pattern: @override void dispose() { _sub?.cancel(); _controller.dispose(); _focusNode.dispose(); super.dispose(); }. 5) WeakReference for optional references. 6) Profile: DevTools > Memory > Diff snapshots before/after navigation to find retained widgets."
        },
        {
            "instruction": "How do you optimize widget rebuild performance in Flutter?",
            "input": "",
            "output": "Minimize rebuilds: 1) const constructors: const Text('Hello') never rebuilds. 2) Extract widgets: break large build methods into smaller StatelessWidgets. 3) Use Selector/Consumer in Provider to rebuild only affected parts. 4) Avoid rebuilding entire lists: use keys for stable identity. 5) RepaintBoundary isolates paint calls. 6) late final for computed values. 7) didUpdateWidget check: if (old.id != widget.id) refetch();. 8) debugPrintRebuildDirtyWidgets = true to track rebuilds. 9) Use AnimatedBuilder instead of addListener+setState."
        },
        {
            "instruction": "How do you implement shader compilation jank mitigation?",
            "input": "",
            "output": "Shader warmup prevents first-frame jank from SKSL compilation. 1) Capture shaders: flutter run --profile --cache-sksl --purge-persistent-cache. Run through all animations, then press 'M' in terminal. Saves flutter_01.sksl.json. 2) Bundle: flutter build apk --bundle-sksl-path=flutter_01.sksl.json. 3) Impeller (iOS default, Android preview) eliminates SKSL jank by pre-compiling all shaders. Enable: --enable-impeller. 4) Reduce custom shaders and complex effects. 5) Warm up common operations in splash screen."
        },
        # Architecture Patterns
        {
            "instruction": "How do you implement MVVM architecture in Flutter?",
            "input": "",
            "output": "MVVM separates Model-View-ViewModel. Model: plain data classes + repository. ViewModel: class UserViewModel extends ChangeNotifier { final UserRepository _repo; List<User> _users = []; bool _loading = false; List<User> get users => _users; bool get loading => _loading; Future<void> loadUsers() async { _loading = true; notifyListeners(); _users = await _repo.getUsers(); _loading = false; notifyListeners(); } }. View: Consumer<UserViewModel>(builder: (ctx, vm, _) { if (vm.loading) return CircularProgressIndicator(); return UserList(vm.users); }). ViewModel holds UI state, exposes actions, never imports Flutter widgets."
        },
        {
            "instruction": "How do you implement the BLoC pattern with Freezed for immutable states?",
            "input": "",
            "output": "@freezed class UserState with _$UserState { const factory UserState.initial() = _Initial; const factory UserState.loading() = _Loading; const factory UserState.loaded(List<User> users) = _Loaded; const factory UserState.error(String message) = _Error; }. @freezed class UserEvent with _$UserEvent { const factory UserEvent.fetch() = _Fetch; const factory UserEvent.delete(int id) = _Delete; }. class UserBloc extends Bloc<UserEvent, UserState> { UserBloc(this._repo) : super(UserState.initial()) { on<_Fetch>((e, emit) async { emit(UserState.loading()); final users = await _repo.getUsers(); emit(UserState.loaded(users)); }); } }. UI uses state.when(initial: ..., loading: ..., loaded: ..., error: ...)."
        },
        {
            "instruction": "How do you implement modular architecture in Flutter?",
            "input": "",
            "output": "Modular architecture splits features into independent packages. Structure: packages/core (shared utilities, theme, network), packages/auth (login/register), packages/home (dashboard), packages/profile, app/ (composition root). Each module: lib/src/ (implementation), lib/module.dart (public API). Use Melos for monorepo management: melos bootstrap links local packages. pubspec.yaml dependencies: auth: path: ../packages/auth. Module communication via interfaces defined in core. DI wires modules at app level. Benefits: team scalability, independent testing, faster builds with incremental compilation."
        },
        {
            "instruction": "How do you implement the Command pattern in Flutter?",
            "input": "",
            "output": "Command pattern encapsulates actions as objects for undo/redo. abstract class Command { void execute(); void undo(); }. class AddItemCommand implements Command { final List<Item> list; final Item item; AddItemCommand(this.list, this.item); void execute() => list.add(item); void undo() => list.remove(item); }. CommandManager: class CommandManager { final _history = <Command>[]; int _current = -1; void execute(Command cmd) { cmd.execute(); _history.add(cmd); _current++; } void undo() { if (_current >= 0) _history[_current--].undo(); } void redo() { if (_current < _history.length - 1) _history[++_current].execute(); } }."
        },
        # Platform Channels
        {
            "instruction": "How do you create a custom method channel plugin?",
            "input": "",
            "output": "Dart side: class NativeBattery { static const _channel = MethodChannel('com.app/battery'); static Future<int> getBatteryLevel() async { final level = await _channel.invokeMethod<int>('getBatteryLevel'); return level ?? -1; } }. Android (Kotlin): class MainActivity : FlutterActivity() { override fun configureFlutterEngine(engine: FlutterEngine) { MethodChannel(engine.dartExecutor.binaryMessenger, 'com.app/battery').setMethodCallHandler { call, result -> when (call.method) { \"getBatteryLevel\" -> { val level = getBattery(); result.success(level) } else -> result.notImplemented() } } } }. iOS: similar with FlutterMethodChannel."
        },
        {
            "instruction": "How do you implement EventChannel for streaming platform data?",
            "input": "",
            "output": "EventChannel streams continuous data from native to Dart. Dart: final _channel = EventChannel('com.app/sensor'); Stream<double> get sensorStream => _channel.receiveBroadcastStream().map((event) => event as double);. Use: StreamBuilder(stream: sensorStream, builder: ...). Android: EventChannel(messenger, 'com.app/sensor').setStreamHandler(object : EventChannel.StreamHandler { override fun onListen(args: Any?, sink: EventChannel.EventSink) { sensorManager.registerListener(object : SensorEventListener { override fun onSensorChanged(event: SensorEvent) { sink.success(event.values[0]) } }, sensor, NORMAL) } override fun onCancel(args: Any?) { sensorManager.unregisterListener(listener) } })."
        },
        {
            "instruction": "How do you implement Pigeon for type-safe platform channels?",
            "input": "",
            "output": "Pigeon generates type-safe platform channel code. Define API in Dart: @HostApi() abstract class UserApi { UserResponse getUser(int userId); } class UserResponse { String? name; int? age; }. Generate: dart run pigeon --input pigeons/user_api.dart --dart_out lib/user_api.g.dart --kotlin_out android/.../UserApi.kt --swift_out ios/.../UserApi.swift. Implement on native: class UserApiImpl : UserApi { override fun getUser(userId: Long): UserResponse { return UserResponse(name = \"John\", age = 25) } }. Register: UserApi.setUp(flutterEngine.dartExecutor, UserApiImpl()). No manual serialization — Pigeon handles encoding."
        },
        # Testing Advanced
        {
            "instruction": "How do you write integration tests in Flutter?",
            "input": "",
            "output": "Integration tests run on real devices. Setup: add integration_test dependency. Create integration_test/app_test.dart: import 'package:integration_test/integration_test.dart'; void main() { IntegrationTestWidgetsFlutterBinding.ensureInitialized(); testWidgets('full flow', (tester) async { await tester.pumpWidget(MyApp()); await tester.tap(find.text('Login')); await tester.pumpAndSettle(); await tester.enterText(find.byType(TextField).first, 'user@test.com'); await tester.tap(find.text('Submit')); await tester.pumpAndSettle(); expect(find.text('Welcome'), findsOneWidget); }); }. Run: flutter test integration_test/app_test.dart."
        },
        {
            "instruction": "How do you implement golden tests in Flutter?",
            "input": "",
            "output": "Golden tests compare widget rendering against reference images. testWidgets('button golden', (tester) async { await tester.pumpWidget(MaterialApp(home: MyButton())); await expectLater(find.byType(MyButton), matchesGoldenFile('goldens/my_button.png')); });. Generate: flutter test --update-goldens. Comparison: flutter test (fails if pixels differ). Configure threshold: goldenFileComparator = TolerantComparator(Uri.parse('test/goldens'), precisionTolerance: 0.01);. Platform-dependent rendering: use CI for consistent results. Font loading: await loadAppFonts() for custom fonts in tests."
        },
        {
            "instruction": "How do you test BLoC/Cubit components?",
            "input": "",
            "output": "Use bloc_test package. blocTest<CounterCubit, int>('emits [1] when increment called', build: () => CounterCubit(), act: (cubit) => cubit.increment(), expect: () => [1]);. BLoC test: blocTest<UserBloc, UserState>('emits [loading, loaded] on fetch', build: () => UserBloc(mockRepo), setUp: () => when(mockRepo.getUsers()).thenAnswer((_) async => [User('John')]), act: (bloc) => bloc.add(FetchUsers()), expect: () => [UserState.loading(), UserState.loaded([User('John')])], verify: (_) => verify(mockRepo.getUsers()).called(1));. Test error states, edge cases, and state transitions."
        },
        {
            "instruction": "How do you implement test coverage reporting in Flutter?",
            "input": "",
            "output": "Generate: flutter test --coverage. Output: coverage/lcov.info. View HTML report: genhtml coverage/lcov.info -o coverage/html && open coverage/html/index.html. Install genhtml: apt-get install lcov (Linux/Mac). Exclude generated files: flutter test --coverage && lcov --remove coverage/lcov.info '*.g.dart' '*.freezed.dart' -o coverage/filtered.info. CI integration: upload to Codecov/Coveralls. Enforce thresholds: check coverage percentage in CI pipeline. Per-file: lcov --list coverage/lcov.info. VS Code extension: Coverage Gutters shows inline coverage."
        },
        {
            "instruction": "How do you implement end-to-end testing with Patrol?",
            "input": "",
            "output": "Patrol enables native interaction in tests. Setup: add patrol to dev_dependencies, configure patrol section in pubspec.yaml. Test: patrolTest('login flow', ($) async { await $.pumpWidgetAndSettle(MyApp()); await $.tap(find.text('Login')); await $.native.enterTextByIndex('user@test.com', index: 0); await $.native.tap(NativeSelector(text: 'ALLOW')); // handle permission dialog await $.pumpAndSettle(); expect(find.text('Dashboard'), findsOneWidget); });. Run: patrol test. Patrol can interact with native system dialogs, notifications, permissions that Flutter tests can't access."
        },
        # CI/CD & DevOps
        {
            "instruction": "How do you set up GitHub Actions CI/CD for Flutter?",
            "input": "",
            "output": "Create .github/workflows/ci.yml: name: CI; on: [push, pull_request]; jobs: test: runs-on: ubuntu-latest; steps: - uses: actions/checkout@v4; - uses: subosito/flutter-action@v2 with: flutter-version: '3.19.0'; - run: flutter pub get; - run: flutter analyze; - run: flutter test --coverage; - uses: codecov/codecov-action@v3. Build job: - run: flutter build apk --release. Deploy: use fastlane or Firebase App Distribution. Add caching: - uses: actions/cache@v3 with: path: ~/.pub-cache. Matrix test multiple Flutter versions."
        },
        {
            "instruction": "How do you implement Fastlane for Flutter deployment?",
            "input": "",
            "output": "Setup: install fastlane, init in ios/ and android/ directories. iOS lane: lane :beta do build_app(workspace: 'Runner.xcworkspace', scheme: 'Runner'); upload_to_testflight end. Android lane: lane :beta do gradle(task: 'bundle', properties: {'android.injected.signing.key.alias': ENV['KEY_ALIAS']}); upload_to_play_store(track: 'beta', aab: '../build/app/outputs/bundle/release/app-release.aab') end. Appfile: app_identifier, apple_id, json_key_file. Use .env for secrets. Match for iOS code signing. Integrate with CI for automated releases."
        },
        {
            "instruction": "How do you implement CodePush/OTA updates in Flutter?",
            "input": "",
            "output": "Shorebird (Flutter CodePush) enables OTA Dart code updates. Setup: shorebird init, shorebird release android. Push update: shorebird patch android --release-version 1.0.0. How it works: replaces Dart code without app store review. Limitations: can't change native code, assets, or Flutter engine. Alternative: Serverpod for feature flags + remote config. Firebase Remote Config for toggling features without code deployment. OTA reduces deployment friction for bug fixes. Shorebird supports Android and iOS, requires Shorebird account."
        },
        # Advanced Dart Features
        {
            "instruction": "How do you implement custom iterables and generators in Dart?",
            "input": "",
            "output": "Sync generator: Iterable<int> fibonacci() sync* { int a = 0, b = 1; while (true) { yield a; final next = a + b; a = b; b = next; } }. Usage: fibonacci().take(10).toList();. Async generator: Stream<int> countDown(int from) async* { for (var i = from; i >= 0; i--) { await Future.delayed(Duration(seconds: 1)); yield i; } }. yield* delegates to another iterable: Iterable<int> flatten(List<List<int>> lists) sync* { for (var list in lists) yield* list; }. Generators are lazy — values computed on demand."
        },
        {
            "instruction": "How do you implement operator overloading in Dart?",
            "input": "",
            "output": "Override operators with operator keyword: class Vector2 { final double x, y; Vector2(this.x, this.y); Vector2 operator +(Vector2 other) => Vector2(x + other.x, y + other.y); Vector2 operator -(Vector2 other) => Vector2(x - other.x, y - other.y); Vector2 operator *(double scalar) => Vector2(x * scalar, y * scalar); bool operator ==(Object other) => other is Vector2 && x == other.x && y == other.y; int get hashCode => Object.hash(x, y); Vector2 operator -() => Vector2(-x, -y); double operator [](int index) => index == 0 ? x : y; }. Available operators: +, -, *, /, ~/, %, ==, <, >, <=, >=, [], []=, ~, &, |, ^, <<, >>."
        },
        {
            "instruction": "How do you use Dart zones for error handling and async tracking?",
            "input": "",
            "output": "Zones capture async errors and provide execution context. runZonedGuarded(() { runApp(MyApp()); }, (error, stackTrace) { crashReporter.report(error, stackTrace); });. Zone values: runZoned(() { print(Zone.current[#requestId]); }, zoneValues: {#requestId: 'abc123'});. Override async behavior: runZoned(() { Timer(Duration(seconds: 1), () => print('modified timer')); }, zoneSpecification: ZoneSpecification(createTimer: (self, parent, zone, duration, callback) { print('Timer created'); return parent.createTimer(zone, duration, callback); }));. Used for logging, profiling, error collection."
        },
        {
            "instruction": "How do you implement sealed classes for exhaustive pattern matching?",
            "input": "",
            "output": "Dart 3 sealed classes enable exhaustive switch. sealed class Shape {} class Circle extends Shape { final double radius; Circle(this.radius); } class Rectangle extends Shape { final double w, h; Rectangle(this.w, this.h); } class Triangle extends Shape { final double base, height; Triangle(this.base, this.height); }. Exhaustive switch: double area(Shape s) => switch (s) { Circle(radius: var r) => 3.14159 * r * r, Rectangle(w: var w, h: var h) => w * h, Triangle(base: var b, height: var h) => 0.5 * b * h, };. Compiler ensures all subtypes handled — adding new subtype causes compile error."
        },
        {
            "instruction": "How do you use Dart FFI to call C libraries?",
            "input": "",
            "output": "Dart FFI (Foreign Function Interface) calls native C functions. 1) Load library: final lib = DynamicLibrary.open('libmath.so');. 2) Define types: typedef AddFunc = Int32 Function(Int32, Int32); typedef AddDart = int Function(int, int);. 3) Lookup: final add = lib.lookupFunction<AddFunc, AddDart>('add');. 4) Call: int result = add(3, 4);. Structs: final class Point extends Struct { @Int32() external int x; @Int32() external int y; }. Allocate memory: final pointer = calloc<Point>(); pointer.ref.x = 10; calloc.free(pointer);. Use ffigen to auto-generate bindings from C headers."
        },
        # Advanced State Management
        {
            "instruction": "How do you implement optimistic updates in Flutter?",
            "input": "",
            "output": "Optimistic updates assume success and revert on failure. Pattern: void addTodo(Todo todo) { final previousState = List<Todo>.from(state.todos); // Optimistic: update UI immediately emit(state.copyWith(todos: [...state.todos, todo])); try { await _repo.createTodo(todo); } catch (e) { // Revert on failure emit(state.copyWith(todos: previousState)); emit(state.copyWith(error: 'Failed to add')); } }. Benefits: instant UI feedback. Apply to likes, comments, cart operations. Track pending operations for sync indicators. Use unique temporary IDs replaced by server IDs on success."
        },
        {
            "instruction": "How do you implement state machines in Flutter with Bloc?",
            "input": "",
            "output": "State machines enforce valid state transitions. sealed class AuthState {} class Unauthenticated extends AuthState {} class Authenticating extends AuthState {} class Authenticated extends AuthState { final User user; Authenticated(this.user); } class AuthError extends AuthState { final String message; AuthError(this.message); }. class AuthBloc extends Bloc<AuthEvent, AuthState> { AuthBloc() : super(Unauthenticated()) { on<LoginRequested>((event, emit) async { if (state is! Unauthenticated && state is! AuthError) return; // guard emit(Authenticating()); try { final user = await _auth.login(event.email, event.password); emit(Authenticated(user)); } catch (e) { emit(AuthError(e.toString())); } }); } }."
        },
        {
            "instruction": "How do you implement multi-provider architecture in Flutter?",
            "input": "",
            "output": "MultiProvider organizes multiple state providers. MultiProvider(providers: [Provider<ApiService>(create: (_) => ApiServiceImpl()), Provider<LocalDb>(create: (_) => LocalDbImpl()), ChangeNotifierProxyProvider2<ApiService, LocalDb, UserRepository>(create: (_) => UserRepository(), update: (_, api, db, repo) => repo!..init(api, db)), ChangeNotifierProvider(create: (ctx) => AuthViewModel(ctx.read<UserRepository>())), ChangeNotifierProvider(create: (ctx) => ThemeViewModel())], child: MyApp());. Layer: services → repositories → view models. ProxyProvider for dependencies between providers."
        },
        # Advanced UI
        {
            "instruction": "How do you implement a custom render object in Flutter?",
            "input": "",
            "output": "Custom RenderObject for layout/painting control. class DotWidget extends LeafRenderObjectWidget { final Color color; final double size; DotWidget({required this.color, required this.size}); @override RenderDot createRenderObject(context) => RenderDot(color: color, size: size); @override void updateRenderObject(context, RenderDot renderObject) { renderObject..color = color..size = size; } } class RenderDot extends RenderBox { Color color; double size; RenderDot({required this.color, required this.size}); @override void performLayout() { this.size = constraints.constrain(Size(size, size)); } @override void paint(PaintingContext context, Offset offset) { context.canvas.drawCircle(offset + Offset(size/2, size/2), size/2, Paint()..color = color); } }."
        },
        {
            "instruction": "How do you implement complex scroll effects with SliverPersistentHeaderDelegate?",
            "input": "",
            "output": "class MySliverHeaderDelegate extends SliverPersistentHeaderDelegate { @override double get minExtent => 60; @override double get maxExtent => 200; @override Widget build(BuildContext context, double shrinkOffset, bool overlapsContent) { final progress = shrinkOffset / (maxExtent - minExtent); return Container(color: Color.lerp(Colors.blue, Colors.indigo, progress), child: Stack(children: [Positioned(left: 16, bottom: 16, child: Opacity(opacity: 1 - progress, child: Text('Expanded Title', style: TextStyle(fontSize: 24)))), Positioned(left: 16 + (40 * progress), top: 16, child: Text('Title', style: TextStyle(fontSize: 16 + (8 * (1 - progress)))))])); } @override bool shouldRebuild(old) => true; }. Use in CustomScrollView with SliverPersistentHeader(delegate: MySliverHeaderDelegate(), pinned: true)."
        },
        {
            "instruction": "How do you implement custom implicit animations in Flutter?",
            "input": "",
            "output": "Extend ImplicitlyAnimatedWidget: class AnimatedColor extends ImplicitlyAnimatedWidget { final Color color; final Widget child; AnimatedColor({required this.color, required this.child, required Duration duration}) : super(duration: duration); @override AnimatedColorState createState() => AnimatedColorState(); } class AnimatedColorState extends AnimatedWidgetBaseState<AnimatedColor> { ColorTween? _colorTween; @override void forEachTween(visitor) { _colorTween = visitor(_colorTween, widget.color, (v) => ColorTween(begin: v as Color)) as ColorTween?; } @override Widget build(context) => ColoredBox(color: _colorTween!.evaluate(animation)!, child: widget.child); }. Auto-animates when color property changes."
        },
        {
            "instruction": "How do you implement a custom layout delegate?",
            "input": "",
            "output": "Use CustomMultiChildLayout with MultiChildLayoutDelegate. class DashboardLayoutDelegate extends MultiChildLayoutDelegate { @override void performLayout(Size size) { if (hasChild('header')) { layoutChild('header', BoxConstraints.tightFor(width: size.width, height: 60)); positionChild('header', Offset.zero); } if (hasChild('sidebar')) { final sidebarSize = layoutChild('sidebar', BoxConstraints(maxWidth: 250, maxHeight: size.height - 60)); positionChild('sidebar', Offset(0, 60)); } if (hasChild('content')) { layoutChild('content', BoxConstraints(maxWidth: size.width - 250, maxHeight: size.height - 60)); positionChild('content', Offset(250, 60)); } } @override bool shouldRelayout(old) => false; }. Children use LayoutId(id: 'header', child: ...)."
        },
        {
            "instruction": "How do you implement animated theme transitions in Flutter?",
            "input": "",
            "output": "Smooth theme switching: 1) AnimatedTheme: AnimatedTheme(data: _isDark ? darkTheme : lightTheme, duration: Duration(ms: 500), child: Builder(builder: (ctx) => Scaffold(...))); 2) Custom: wrap MaterialApp in AnimatedBuilder listening to theme controller. 3) Page transition effect: stack current view → capture screenshot → animate reveal new theme. animate_do package for entrance animations. Hero-style theme switch: CircularRevealAnimation expanding from toggle button position using CustomClipper with animating radius."
        },
        # Security & Auth Advanced
        {
            "instruction": "How do you implement OAuth2/OpenID Connect in Flutter?",
            "input": "",
            "output": "Use flutter_appauth package for RFC-compliant flow. final result = await FlutterAppAuth().authorizeAndExchangeCode(AuthorizationTokenRequest('client_id', 'com.app:/callback', discoveryUrl: 'https://auth.server/.well-known/openid-configuration', scopes: ['openid', 'profile', 'email']));. Store tokens: await secureStorage.write(key: 'access_token', value: result.accessToken);. Refresh: final refreshResult = await FlutterAppAuth().token(TokenRequest('client_id', 'com.app:/callback', refreshToken: storedRefreshToken));. Add Dio interceptor for auto-refresh on 401. PKCE is used by default for security."
        },
        {
            "instruction": "How do you implement JWT token management in Flutter?",
            "input": "",
            "output": "JWT management pattern: class AuthManager { final _storage = FlutterSecureStorage(); Future<String?> get accessToken => _storage.read(key: 'access'); bool isTokenExpired(String token) { final payload = json.decode(utf8.decode(base64Url.decode(token.split('.')[1].padRight(4 - token.split('.')[1].length % 4 + token.split('.')[1].length, '=')))); return DateTime.fromMillisecondsSinceEpoch(payload['exp'] * 1000).isBefore(DateTime.now()); } }. Dio interceptor: onRequest check expiry → refresh if needed → attach header. onError 401 → refresh → retry. Use dart_jsonwebtoken for parsing. Never store tokens in SharedPreferences — use SecureStorage."
        },
        {
            "instruction": "How do you implement end-to-end encryption in Flutter?",
            "input": "",
            "output": "E2E encryption with pointycastle package. Key generation: final keyPair = RSAKeyGenerator()..init(ParametersWithRandom(RSAKeyGeneratorParameters(2048, 65537, 5), secureRandom)); final pair = keyPair.generateKeyPair();. AES encryption: final key = AESFastEngine(); final params = PaddedBlockCipherParameters(KeyParameter(keyBytes), null); final cipher = PaddedBlockCipher('AES/CBC/PKCS7')..init(true, params); final encrypted = cipher.process(plainText);. Hybrid approach: RSA for key exchange, AES for data. Use encrypt package for simpler API. Store private keys in secure storage. Signal Protocol via libsignal_protocol_dart for messaging."
        },
        # Advanced Navigation
        {
            "instruction": "How do you implement Navigator 2.0 (Router API)?",
            "input": "",
            "output": "Navigator 2.0 declarative routing. MaterialApp.router(routerDelegate: MyRouterDelegate(), routeInformationParser: MyRouteParser()). class MyRouterDelegate extends RouterDelegate<AppRoute> with ChangeNotifier, PopNavigatorRouterDelegateMixin { final _navigatorKey = GlobalKey<NavigatorState>(); AppRoute? _currentRoute; @override Widget build(context) => Navigator(key: _navigatorKey, pages: [MaterialPage(child: HomePage()), if (_currentRoute?.isDetail ?? false) MaterialPage(child: DetailPage(_currentRoute!.id))], onPopPage: (route, result) { if (!route.didPop(result)) return false; _currentRoute = null; notifyListeners(); return true; }); }. Complex but enables deep linking and web URLs."
        },
        {
            "instruction": "How do you implement dynamic feature modules in Flutter?",
            "input": "",
            "output": "Deferred loading splits code into downloadable units. import 'heavy_feature.dart' deferred as heavy; Future<void> loadFeature() async { await heavy.loadLibrary(); Navigator.push(context, MaterialPageRoute(builder: (_) => heavy.HeavyFeatureScreen())); }. Show loading: FutureBuilder(future: heavy.loadLibrary(), builder: (ctx, snap) { if (snap.connectionState != ConnectionState.done) return CircularProgressIndicator(); return heavy.Widget(); });. Each deferred import creates a separate JS file (web) or loading unit. Plan split points at feature boundaries. Monitor sizes with --analyze-size."
        },
        # Advanced Firebase
        {
            "instruction": "How do you implement Firestore offline persistence and conflict resolution?",
            "input": "",
            "output": "Firestore has built-in offline support. Enable: FirebaseFirestore.instance.settings = Settings(persistenceEnabled: true, cacheSizeBytes: Settings.CACHE_SIZE_UNLIMITED);. Offline writes are queued and synced: firestore.collection('todos').add({'title': 'test', 'timestamp': FieldValue.serverTimestamp()});. Listen with metadata: snapshots(includeMetadataChanges: true).listen((snap) { final isFromCache = snap.metadata.isFromCache; });. Conflict resolution: last-write-wins by default. For custom: use transactions: firestore.runTransaction((txn) async { final doc = await txn.get(ref); txn.update(ref, {'count': doc['count'] + 1}); });."
        },
        {
            "instruction": "How do you implement Firebase Analytics with custom events?",
            "input": "",
            "output": "Setup: await Firebase.initializeApp(); final analytics = FirebaseAnalytics.instance;. Log events: await analytics.logEvent(name: 'purchase', parameters: {'item_id': 'SKU123', 'value': 9.99, 'currency': 'USD'});. Screen tracking: analytics.logScreenView(screenName: 'ProductDetail', screenClass: 'ProductDetailScreen');. User properties: analytics.setUserProperty(name: 'subscription', value: 'premium');. NavigatorObserver: MaterialApp(navigatorObservers: [FirebaseAnalyticsObserver(analytics: analytics)]);. Debug: adb shell setprop debug.firebase.analytics.app com.example.app for real-time DebugView."
        },
        # Accessibility Advanced
        {
            "instruction": "How do you implement custom semantics for complex widgets?",
            "input": "",
            "output": "Semantics widget wraps complex UI for screen readers. Semantics(label: 'Play button, currently paused', button: true, onTap: () => play(), child: CustomPaintedButton());. MergeSemantics: combines child tree into single node. ExcludeSemantics: hides decorative elements. Semantics.fromProperties for detailed control: SemanticsProperties(label: 'Rating: 4 out of 5 stars', value: '4', increasedValue: '5', decreasedValue: '3', onIncrease: () => rate(5), onDecrease: () => rate(3)). Custom actions: semantics.customSemanticsActions = {CustomSemanticsAction(label: 'Bookmark'): () => bookmark()}. Test: expect(tester.getSemantics(find.byType(MyWidget)), matchesSemantics(label: 'Play'))."
        },
        # Advanced Build & Deployment
        {
            "instruction": "How do you implement Flutter module embedding in existing native apps?",
            "input": "",
            "output": "Add-to-app embeds Flutter in existing Android/iOS apps. Create module: flutter create --template module my_flutter. Android: settings.gradle: setBinding(new Binding([gradle: this])); evaluate(new File('../my_flutter/.android/include_flutter.groovy')). Add dependency: implementation project(':flutter'). Launch: startActivity(FlutterActivity.createDefaultIntent(this)). Fragment: FlutterFragment.createDefault(). iOS: add Flutter via CocoaPods. FlutterEngine warmup: let engine = FlutterEngine(name: 'my_engine'); engine.run();. Use FlutterViewController(engine: engine). Multiple engines: FlutterEngineGroup for memory-efficient multiple instances."
        },
        {
            "instruction": "How do you implement custom Flutter engine configuration?",
            "input": "",
            "output": "FlutterEngine configuration: Android: FlutterEngine(context).apply { dartExecutor.executeDartEntrypoint(DartExecutor.DartEntrypoint(FlutterInjector.instance().flutterLoader().findAppBundlePath(), 'main')); navigationChannel.setInitialRoute('/custom'); }. iOS: let engine = FlutterEngine(); engine.run(withEntrypoint: 'main', initialRoute: '/custom');. Multi-engine: FlutterEngineGroup creates engines sharing resources. Configure: GeneratedPluginRegistrant.register(with: engine). Custom entrypoints: @pragma('vm:entry-point') void customMain() => runApp(MyModule());. Warm up engines in Application.onCreate for faster startup."
        },
        # Reactive Programming
        {
            "instruction": "How do you use RxDart for reactive programming in Flutter?",
            "input": "",
            "output": "RxDart extends Dart streams with reactive operators. Subjects: final subject = BehaviorSubject<int>.seeded(0); subject.add(1); subject.stream.listen(print);. PublishSubject (no initial value), ReplaySubject (replay N values). Operators: stream.debounceTime(Duration(ms: 300)).switchMap((query) => searchApi(query)).doOnData((data) => cache(data)).handleError((e) => showError(e)).listen((results) => updateUI(results));. CombineLatest: Rx.combineLatest2(nameStream, emailStream, (name, email) => FormState(name, email));. MergeStream, ZipStream, ConcatStream for combining multiple streams."
        },
        {
            "instruction": "How do you implement reactive form validation with streams?",
            "input": "",
            "output": "Stream-based form validation: class LoginBloc { final _email = BehaviorSubject<String>(); final _password = BehaviorSubject<String>(); Stream<String> get email => _email.stream.transform(StreamTransformer.fromHandlers(handleData: (value, sink) { if (value.contains('@')) sink.add(value); else sink.addError('Invalid email'); })); Stream<bool> get isValid => Rx.combineLatest2(email, password, (e, p) => true); Function(String) get changeEmail => _email.sink.add; void dispose() { _email.close(); _password.close(); } }. UI: StreamBuilder<String>(stream: bloc.email, builder: (ctx, snap) => TextField(errorText: snap.error?.toString()))."
        },
        # Database Advanced
        {
            "instruction": "How do you implement Drift (formerly Moor) for type-safe database access?",
            "input": "",
            "output": "Drift provides type-safe SQL with code generation. class AppDatabase extends _$AppDatabase { AppDatabase() : super(NativeDatabase.createInBackground(File('db.sqlite'))); @override int get schemaVersion => 1; } class Users extends Table { IntColumn get id => integer().autoIncrement()(); TextColumn get name => text().withLength(min: 1, max: 50)(); DateTimeColumn get createdAt => dateTime().withDefault(currentDateAndTime)(); } // Generated: Future<List<User>> getAllUsers() => select(users).get(); Future<int> addUser(UsersCompanion entry) => into(users).insert(entry); Stream<List<User>> watchUsers() => select(users).watch();. Migrations: @override MigrationStrategy get migration => MigrationStrategy(onCreate: ..., onUpgrade: ...)."
        },
        {
            "instruction": "How do you implement real-time database sync with Supabase in Flutter?",
            "input": "",
            "output": "Supabase real-time: final supabase = Supabase.instance.client;. Query: final data = await supabase.from('todos').select().eq('user_id', uid);. Insert: await supabase.from('todos').insert({'title': 'New', 'user_id': uid});. Real-time: supabase.from('todos').stream(primaryKey: ['id']).eq('user_id', uid).listen((data) { setState(() => todos = data); });. Auth: await supabase.auth.signInWithPassword(email: email, password: pass);. RLS policies for security. Supabase.initialize(url: url, anonKey: key) in main. Edge functions for server-side logic."
        },
        # Concurrency & Performance
        {
            "instruction": "How do you implement compute-heavy tasks without blocking the UI?",
            "input": "",
            "output": "Approaches: 1) compute(): final result = await compute(parseJson, jsonString); — spawns isolate for single computation. 2) Isolate.run(): await Isolate.run(() => heavyCalculation()); — Dart 2.19+. 3) Long-running isolate with ports: final receivePort = ReceivePort(); await Isolate.spawn(workerEntry, receivePort.sendPort); receivePort.listen((msg) => handleResult(msg));. 4) flutter_isolate for isolates with plugin access. 5) Worker pool: spawn N isolates, dispatch tasks round-robin. Rules: pass only serializable data, can't access UI or plugins from standard isolates."
        },
        {
            "instruction": "How do you implement a custom InheritedWidget?",
            "input": "",
            "output": "InheritedWidget efficiently passes data down the tree. class ThemeConfig extends InheritedWidget { final Color primaryColor; final double fontSize; const ThemeConfig({required this.primaryColor, required this.fontSize, required Widget child}) : super(child: child); static ThemeConfig of(BuildContext context) => context.dependOnInheritedWidgetOfExactType<ThemeConfig>()!; static ThemeConfig? maybeOf(BuildContext context) => context.dependOnInheritedWidgetOfExactType<ThemeConfig>(); @override bool updateShouldNotify(ThemeConfig old) => primaryColor != old.primaryColor || fontSize != old.fontSize; }. Usage: ThemeConfig(primaryColor: Colors.blue, fontSize: 16, child: App()). Access: ThemeConfig.of(context).primaryColor. O(1) lookup, rebuilds dependents on change."
        },
        {
            "instruction": "How do you implement background geolocation tracking in Flutter?",
            "input": "",
            "output": "Use geolocator + flutter_background_service. Setup: final service = FlutterBackgroundService(); await service.configure(androidConfiguration: AndroidConfiguration(onStart: onStart, isForegroundMode: true, notificationChannelId: 'location', notificationTitle: 'Tracking'), iosConfiguration: IosConfiguration(autoStart: true));. @pragma('vm:entry-point') void onStart(ServiceInstance service) { Timer.periodic(Duration(seconds: 30), (_) async { final pos = await Geolocator.getCurrentPosition(); service.invoke('locationUpdate', {'lat': pos.latitude, 'lng': pos.longitude}); }); }. Listen: service.on('locationUpdate').listen((data) => updateMap(data)). Request background location permission."
        },
        # Advanced Packages & Ecosystem
        {
            "instruction": "How do you implement code generation with Freezed for data classes?",
            "input": "",
            "output": "@freezed class User with _$User { const factory User({required String name, required int age, @Default('') String email, List<String>? tags}) = _User; factory User.fromJson(Map<String, dynamic> json) => _$UserFromJson(json); }. Features: immutable, copyWith: user.copyWith(name: 'Jane'). Pattern matching with union types: @freezed class Result<T> with _$Result<T> { const factory Result.success(T data) = Success; const factory Result.error(String msg) = Error; }. result.when(success: (data) => show(data), error: (msg) => showError(msg)). Run: dart run build_runner build. Generates ==, hashCode, toString, copyWith, fromJson/toJson."
        },
        {
            "instruction": "How do you implement auto_route for advanced navigation?",
            "input": "",
            "output": "auto_route generates type-safe routing. Define: @AutoRouterConfig() class AppRouter extends $AppRouter { @override List<AutoRoute> get routes => [AutoRoute(page: HomeRoute.page, initial: true), AutoRoute(page: UserRoute.page, path: '/user/:id'), AutoRoute(page: SettingsRoute.page, guards: [AuthGuard])]; }. Screen: @RoutePage() class HomePage extends StatelessWidget. Navigate: context.router.push(UserRoute(id: 42));. Guards: class AuthGuard extends AutoRouteGuard { @override void onNavigation(resolver, router) { if (isAuth) resolver.next(); else resolver.redirect(LoginRoute()); } }. Run: dart run build_runner build."
        },
        {
            "instruction": "How do you implement GetIt with Injectable for dependency injection?",
            "input": "",
            "output": "injectable generates GetIt registrations. @module abstract class AppModule { @lazySingleton ApiService get apiService => ApiServiceImpl(); }. @injectable class UserRepository { final ApiService _api; UserRepository(this._api); }. @singleton class AuthService { }. Setup: @InjectableInit() void configureDependencies() => getIt.init();. Environments: @Environment('dev') @injectable class MockApi implements ApiService {}. Register: getIt.init(environment: 'dev');. Run: dart run build_runner build. Access: getIt<UserRepository>(). @preResolve for async factories."
        },
        # Flutter Internals
        {
            "instruction": "How does Flutter's rendering pipeline work internally?",
            "input": "",
            "output": "Flutter's rendering pipeline: 1) Animation phase: Ticker callbacks run, AnimationControllers update values. 2) Build phase: dirty widgets rebuild, Element tree updates, creates/updates RenderObjects. 3) Layout phase: RenderObjects compute sizes/positions. Constraints go down (parent → child), sizes go up (child → parent). 4) Paint phase: RenderObjects paint to Layer tree. RepaintBoundary creates separate layers. 5) Compositing: layers sent to engine. Engine rasterizes via Skia/Impeller on GPU thread. Frame budget: 16.67ms (60fps) or 8.33ms (120fps). Build and layout are interleaved for efficiency."
        },
        {
            "instruction": "How does the Element tree differ from the Widget tree in Flutter?",
            "input": "",
            "output": "Widget tree: immutable configuration blueprints, recreated on rebuild. Element tree: mutable objects managing lifecycle, persistent across rebuilds. RenderObject tree: handles layout/painting, attached to elements. When setState() is called: widget rebuilds (new widget instance), element compares old vs new widget (canUpdate checks runtimeType and key), if same type: element updates with new widget (updateRenderObject). If different: old element unmounted, new created. Elements hold State objects — that's why State persists across rebuilds. Keys force element recreation when needed. InheritedElement enables O(1) ancestor lookup."
        },
        {
            "instruction": "How does Flutter's tree shaking and dead code elimination work?",
            "input": "",
            "output": "Dart AOT compiler performs tree shaking in release builds. Process: 1) Start from main() entry point. 2) Trace all reachable code through static analysis. 3) Unreferenced classes, methods, and functions are excluded from compiled output. 4) --tree-shake-icons removes unused Material/Cupertino icon glyphs (reduces ~100KB). 5) Conditional imports ensure platform-specific code is excluded. 6) const constructors are evaluated at compile time. 7) Dead branches after const bool checks are eliminated. Verify: flutter build --analyze-size. Deferred imports + tree shaking = optimal bundle sizes."
        },
        # Advanced Error Handling
        {
            "instruction": "How do you implement a crash reporting pipeline in Flutter?",
            "input": "",
            "output": "Comprehensive crash reporting: void main() { runZonedGuarded(() async { WidgetsFlutterBinding.ensureInitialized(); FlutterError.onError = (details) { FirebaseCrashlytics.instance.recordFlutterError(details); }; PlatformDispatcher.instance.onError = (error, stack) { FirebaseCrashlytics.instance.recordError(error, stack, fatal: true); return true; }; await Firebase.initializeApp(); if (kReleaseMode) { await FirebaseCrashlytics.instance.setCrashlyticsCollectionEnabled(true); } runApp(MyApp()); }, (error, stack) { FirebaseCrashlytics.instance.recordError(error, stack); }); }. Add user context: Crashlytics.setUserIdentifier(userId). Custom keys: Crashlytics.setCustomKey('screen', 'checkout')."
        },
        {
            "instruction": "How do you implement structured error handling with Either type?",
            "input": "",
            "output": "Either from dartz or fpdart package represents success or failure. Future<Either<Failure, User>> getUser(int id) async { try { final response = await api.get('/users/$id'); return Right(User.fromJson(response.data)); } on DioException catch (e) { return Left(NetworkFailure(e.message ?? '')); } on FormatException { return Left(ParseFailure('Invalid response format')); } }. Usage: final result = await getUser(1); result.fold((failure) => showError(failure.message), (user) => showUser(user));. Chain: result.map((user) => user.name).getOrElse(() => 'Unknown');. Compose: getUser(1).flatMap((user) => getOrders(user.id))."
        },
        # Advanced Animation
        {
            "instruction": "How do you implement Rive animations in Flutter?",
            "input": "",
            "output": "Rive provides design-tool-created interactive animations. Add rive package. Load: RiveAnimation.asset('assets/animation.riv', fit: BoxFit.cover, onInit: (artboard) { final controller = StateMachineController.fromArtboard(artboard, 'StateMachine'); artboard.addController(controller!); _trigger = controller.findInput<bool>('isHovered') as SMIBool; });. Trigger: _trigger.value = true;. Network: RiveAnimation.network(url). State machines enable interactive animations responding to user input. Benefits over Lottie: interactive state machines, smaller files, runtime control. Export from Rive editor."
        },
        {
            "instruction": "How do you implement Lottie animations in Flutter?",
            "input": "",
            "output": "Use lottie package for After Effects animations. Lottie.asset('assets/animation.json', width: 200, height: 200, fit: BoxFit.cover);. With controller: Lottie.asset('animation.json', controller: _controller, onLoaded: (composition) { _controller.duration = composition.duration; _controller.forward(); });. Network: Lottie.network(url). Repeat: repeat: true. Frame range: _controller.value = 0.5 for specific frame. Delegates for dynamic properties: LottieDelegates(values: [ValueDelegate.color(['**'], value: Colors.red)]). Cache: Lottie.asset('anim.json', frameRate: FrameRate.max)."
        },
        {
            "instruction": "How do you implement particle effects in Flutter?",
            "input": "",
            "output": "Custom particle system with CustomPainter: class ParticleSystem { List<Particle> particles = []; void emit(Offset position, int count) { particles.addAll(List.generate(count, (_) => Particle(position: position, velocity: Offset(random.nextDouble() * 4 - 2, random.nextDouble() * -4), life: 1.0, color: Colors.orange))); } void update(double dt) { for (var p in particles) { p.position += p.velocity * dt; p.velocity += Offset(0, 9.8 * dt); // gravity p.life -= dt; } particles.removeWhere((p) => p.life <= 0); } }. Paint in CustomPainter, drive with Ticker. Use for confetti, explosions, snow effects."
        },
        # Monitoring & Observability
        {
            "instruction": "How do you implement performance monitoring in Flutter?",
            "input": "",
            "output": "Firebase Performance: final perf = FirebasePerformance.instance;. Custom trace: final trace = perf.newTrace('data_load'); await trace.start(); await loadData(); trace.setMetric('items_loaded', count); await trace.stop();. HTTP monitoring: final metric = perf.newHttpMetric(url, HttpMethod.Get); await metric.start(); final response = await http.get(url); metric.httpResponseCode = response.statusCode; metric.responseContentType = 'application/json'; metric.responsePayloadSize = response.contentLength; await metric.stop();. Automatic: screen rendering, app startup, HTTP (with monitoring enabled). Custom attributes: trace.putAttribute('user_type', 'premium')."
        },
        {
            "instruction": "How do you implement structured logging in Flutter?",
            "input": "",
            "output": "Structured logging with levels and context: class AppLogger { static void info(String message, {Map<String, dynamic>? context}) { log(message, name: 'APP', level: 800, error: null, stackTrace: null); if (kReleaseMode) { analyticsService.logEvent('log_info', {'message': message, ...?context}); } } static void error(String message, {Object? error, StackTrace? stack}) { log(message, name: 'APP', level: 1000, error: error, stackTrace: stack); if (kReleaseMode) Crashlytics.recordError(error, stack); } }. Use logger package for formatted console output with emoji levels. Filter by level in production."
        },
        # --- Final Advanced Additions ---
        {
            "instruction": "How do you implement custom shader effects in Flutter?",
            "input": "",
            "output": "Flutter supports GLSL fragment shaders. 1) Write shader: #version 460 core; out vec4 fragColor; uniform vec2 uSize; uniform float uTime; void main() { vec2 uv = gl_FragCoord.xy / uSize; fragColor = vec4(uv.x, uv.y, sin(uTime) * 0.5 + 0.5, 1.0); }. 2) Load in Flutter: final program = await FragmentProgram.fromAsset('shaders/effect.frag');. 3) Paint: final shader = program.fragmentShader()..setFloat(0, size.width)..setFloat(1, size.height)..setFloat(2, time); canvas.drawRect(rect, Paint()..shader = shader);. Declare shaders in pubspec.yaml under flutter > shaders."
        },
        {
            "instruction": "How do you implement a custom router with path parameters and query strings?",
            "input": "",
            "output": "GoRouter advanced patterns: GoRouter(routes: [GoRoute(path: '/products', builder: (ctx, state) { final sort = state.uri.queryParameters['sort'] ?? 'name'; final category = state.uri.queryParameters['category']; return ProductListScreen(sort: sort, category: category); }, routes: [GoRoute(path: ':productId', builder: (ctx, state) { final id = state.pathParameters['productId']!; final tab = state.uri.queryParameters['tab'] ?? 'details'; return ProductScreen(id: id, initialTab: tab); })])]);. Navigate: context.go('/products/123?tab=reviews'). Type-safe routes with GoRouterBuilder code generation."
        },
        {
            "instruction": "How do you implement a plugin-based architecture in Flutter?",
            "input": "",
            "output": "Plugin architecture enables extensible apps. Define interfaces: abstract class FeaturePlugin { String get name; Widget buildWidget(BuildContext context); void initialize(); void dispose(); }. Registry: class PluginRegistry { final _plugins = <String, FeaturePlugin>{}; void register(FeaturePlugin plugin) { _plugins[plugin.name] = plugin; plugin.initialize(); } Widget? getWidget(String name, BuildContext ctx) => _plugins[name]?.buildWidget(ctx); List<FeaturePlugin> get all => _plugins.values.toList(); void disposeAll() => _plugins.values.forEach((p) => p.dispose()); }. Register plugins at startup. Feature flags control which plugins load."
        },
        {
            "instruction": "How do you implement advanced text rendering with RichText and TextSpan?",
            "input": "",
            "output": "RichText renders styled text spans. RichText(text: TextSpan(style: DefaultTextStyle.of(context).style, children: [TextSpan(text: 'Bold ', style: TextStyle(fontWeight: FontWeight.bold)), TextSpan(text: 'colored ', style: TextStyle(color: Colors.blue)), TextSpan(text: 'link', style: TextStyle(decoration: TextDecoration.underline, color: Colors.blue), recognizer: TapGestureRecognizer()..onTap = () => launchUrl(url)), WidgetSpan(child: Icon(Icons.star, size: 14))]));. Use Text.rich() shorthand. WidgetSpan embeds inline widgets. Custom InlineSpan for advanced layouts."
        },
        {
            "instruction": "How do you implement a custom keyboard/input accessory view in Flutter?",
            "input": "",
            "output": "Custom keyboard toolbar above software keyboard: Scaffold(body: Column(children: [Expanded(child: content), AnimatedContainer(duration: Duration(ms: 200), height: MediaQuery.of(context).viewInsets.bottom > 0 ? 44 : 0, child: Container(color: Colors.grey[200], child: Row(children: [IconButton(icon: Icon(Icons.format_bold), onPressed: () => insertMarkdown('**')), IconButton(icon: Icon(Icons.format_list_bulleted), onPressed: () => insertMarkdown('- ')), Spacer(), TextButton(onPressed: () => FocusScope.of(context).unfocus(), child: Text('Done'))])))]));. Use InputDecoration.suffixIcon for inline field actions."
        },
        {
            "instruction": "How do you implement A/B testing in Flutter?",
            "input": "",
            "output": "A/B testing with Firebase Remote Config: await remoteConfig.setDefaults({'button_color': 'blue', 'new_checkout': false}); await remoteConfig.fetchAndActivate(); final useNewCheckout = remoteConfig.getBool('new_checkout'); final buttonColor = remoteConfig.getString('button_color');. Show variant: useNewCheckout ? NewCheckoutFlow() : OldCheckoutFlow(). Track: analytics.logEvent(name: 'checkout_variant', parameters: {'variant': useNewCheckout ? 'new' : 'old'});. Analyze in Firebase console. For client-side: hash userId to deterministically assign variant."
        },
        {
            "instruction": "How do you implement app-wide exception boundaries in Flutter?",
            "input": "",
            "output": "Exception boundaries prevent crashes from propagating. class ErrorBoundary extends StatefulWidget { final Widget child; ErrorBoundary({required this.child}); @override State<ErrorBoundary> createState() => _ErrorBoundaryState(); } class _ErrorBoundaryState extends State<ErrorBoundary> { Widget? _errorWidget; @override void initState() { super.initState(); } @override Widget build(context) { if (_errorWidget != null) return _errorWidget!; return widget.child; } }. ErrorWidget.builder = (details) => ErrorBoundary.buildError(details);. Wrap feature modules: ErrorBoundary(child: ChatModule()). Log errors to crash reporting. Show retry button in error UI."
        },
        {
            "instruction": "How do you implement multi-window support in Flutter desktop?",
            "input": "",
            "output": "Multi-window in Flutter desktop using window_manager and multi_window packages. Main: WindowManager.instance.setTitle('Main Window');. New window: final window = await DesktopMultiWindow.createWindow(jsonEncode({'route': '/detail', 'id': 42})); window..setFrame(Rect.fromLTWH(0, 0, 800, 600))..setTitle('Detail')..show();. Entry point: @pragma('vm:entry-point') void detailWindow(List<String> args) { final windowId = int.parse(args[0]); runApp(DetailApp(windowId: windowId)); }. Communication between windows via method channels."
        },
        {
            "instruction": "How do you implement compile-time safety with typedef and type aliases?",
            "input": "",
            "output": "Type aliases improve code readability and safety. typedef Json = Map<String, dynamic>; typedef FromJson<T> = T Function(Json json); typedef Predicate<T> = bool Function(T value);. Usage: Future<Json> fetchData() async { ... }; T parseResponse<T>(Json json, FromJson<T> fromJson) => fromJson(json);. Function types: typedef Callback = void Function(); typedef ValueChanged<T> = void Function(T value); typedef AsyncValueGetter<T> = Future<T> Function();. Extension types (Dart 3.3): extension type UserId(int id) implements int {} — zero-cost wrapper with type safety."
        },
        {
            "instruction": "How do you implement efficient list diffing for large datasets?",
            "input": "",
            "output": "Efficient diffing avoids full list rebuilds. 1) AnimatedList with insertItem/removeItem for granular updates. 2) diffutil_dart package: final diff = calculateListDiff(oldList, newList, detectMoves: true); diff.getUpdatesWithData().forEach((update) { update.when(insert: (pos, data) => _listKey.currentState?.insertItem(pos), remove: (pos, data) => _listKey.currentState?.removeItem(pos, builder), change: (pos, oldData, newData) => setState(() => items[pos] = newData), move: (from, to, data) => moveItem(from, to)); });. Myers diff algorithm runs in O(n*d) time where d is the number of differences."
        },
    ]


def main():
    """Generate and save the raw Flutter Q&A dataset."""
    print("Generating Flutter Q&A dataset...")

    basic = generate_basic_questions()
    intermediate = generate_intermediate_questions()
    advanced = generate_advanced_questions()

    # Tag each sample with its category for later splitting
    for item in basic:
        item["category"] = "basic"
    for item in intermediate:
        item["category"] = "intermediate"
    for item in advanced:
        item["category"] = "advanced"

    all_data = basic + intermediate + advanced

    print(f"  Basic:        {len(basic)} samples")
    print(f"  Intermediate: {len(intermediate)} samples")
    print(f"  Advanced:     {len(advanced)} samples")
    print(f"  Total:        {len(all_data)} samples")

    # Save raw dataset
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, "flutter_qa_raw.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_data, f, indent=2, ensure_ascii=False)

    print(f"\nRaw dataset saved to: {output_path}")
    print("Next step: Run 02_clean_and_split.py to clean and create train/val/test splits.")


if __name__ == "__main__":
    main()
