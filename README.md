# 📖 MotionBook — iOS motion libraries, catalogued for people and agents

[![Platform](https://img.shields.io/badge/platform-iOS-green.svg?style=flat)](https://developer.apple.com/ios/)
![Language](https://img.shields.io/badge/language-Swift-brightgreen.svg?style=flat)
[![License](https://img.shields.io/badge/license-MIT-lightgrey.svg?style=flat)](LICENSE)
[![Catalog](https://img.shields.io/badge/catalog-103%20libraries-ee165b.svg?style=flat)](catalog.json)
[![Refresh](https://github.com/younatics/MotionBook/actions/workflows/refresh.yml/badge.svg)](https://github.com/younatics/MotionBook/actions/workflows/refresh.yml)

<a href="https://apps.apple.com/app/id1205163580"><img src="Images/appstore.png" width="170" height="58" alt="Download on the App Store"></a>

**103 open-source motion, transition and UI libraries for iOS**, with the real thing running inside the [MotionBook app](https://apps.apple.com/app/id1205163580) for 59 of them. Every entry carries its GitHub stars, last push, license, latest tag, how to install it (Swift Package Manager / CocoaPods / Carthage) and, for the live ones, the Xcode version it was last built and run with.

- **People**: browse the list below or the [web catalog](https://younatics.github.io/MotionBook/) with previews.
- **Agents and tools**: read [`catalog.json`](catalog.json) (schema: [`schema/catalog.schema.json`](schema/catalog.schema.json)) or [`llms.txt`](llms.txt). Everything on this page is generated from that file by `scripts/render.py`.
- **Freshness**: GitHub numbers refreshed `2026-10-25` by the weekly [refresh workflow](.github/workflows/refresh.yml); 17 SwiftUI-era libraries, 33 marked inactive (no push since 2021) or archived.

## Use it from an agent

```bash
# all SwiftUI libraries that still get commits, as install lines
curl -s https://raw.githubusercontent.com/younatics/MotionBook/master/catalog.json \
  | jq -r '.libraries[] | select(.tags | index("swiftui")) | select(.archived | not) | .install.spm_package // .url'
```

Each library object has: `title`, `author`, `category`, `summary`, `url`, `tags`, `featured`, `gif`, `stars`, `pushed`, `license`, `archived`, `latest_tag`, `install.{spm,spm_package,cocoapods,carthage}`, `live_demo`, `verified.{date,xcode,ios,via}`.

## Contribute

Add a library with one command and open a pull request — see [CONTRIBUTING.md](CONTRIBUTING.md):

```bash
python3 scripts/refresh_catalog.py --add owner/repo --category Animation --tags swiftui,effects --no-refresh
python3 scripts/render.py
```

## Libraries

Grouped by category, sorted by stars. ★ = GitHub stars · ⟳ = last push · badges: ▶ live in the app, SwiftUI, SPM, CocoaPods, Carthage, Archived / Inactive.

[Animation](#animation) (30) · [Transition](#transition) (16) · [UI](#ui) (20) · [Menu](#menu) (8) · [Alert](#alert) (11) · [Collection View](#collection-view) (7) · [Table View](#table-view) (5) · [Indicator](#indicator) (6)

### Animation

#### [Lottie](https://github.com/airbnb/lottie-ios)
Airbnb · ★ 27K · ⟳ 2026-10 · Apache-2.0 · tag `4.6.1`

Render After Effects animations natively and keep product motion consistent across screens.

`▶ Live demo in the app` · `SPM` · [preview GIF](motion-book/Lottie.gif) · `.package(url: "https://github.com/airbnb/lottie-ios", from: "4.6.1")`

#### [Pop](https://github.com/facebookarchive/pop)
Facebook · ★ 20K · ⟳ 2020-01 · BSD-3-Clause · tag `1.0.11`

Classic extensible animation primitives for spring and decay motion in UIKit apps.

`CocoaPods` · `Archived`

#### [Spring](https://github.com/MengTo/Spring)
MengTo · ★ 14K · ⟳ 2023-07 · MIT · tag `1.0.5`

A library to simplify iOS animations in Swift.

`▶ Live demo in the app` · `CocoaPods` · [preview GIF](motion-book/Spring.gif)

#### [SkeletonView](https://github.com/Juanpe/SkeletonView)
Juanpe · ★ 13K · ⟳ 2026-06 · MIT · tag `1.31.0`

Today almost all apps have async processes, such as Api requests, long running processes, etc. And while the processes are working, usually developers place a loading view to show users that something is going on.SkeletonView has been conceived to address this need, an elegant way to show users that something is happening and also prepare them to which contents he is waiting.

`▶ Live demo in the app` · `SPM` · `CocoaPods` · `Carthage` · [preview GIF](motion-book/SkeletonView.gif) · `.package(url: "https://github.com/Juanpe/SkeletonView", from: "1.31.0")`

#### [FLAnimatedImage](https://github.com/Flipboard/FLAnimatedImage)
Flipboard · ★ 7.9K · ⟳ 2024-03 · MIT · tag `1.0.17`

FLAnimatedImage is a performant animated GIF engine for iOS: 1. Plays multiple GIFs simultaneously with a playback speed comparable to desktop browsers 2. Honors variable frame delays 3. Behaves gracefully under memory pressure 4. Eliminates delays or blocking during the first playback loop 5. Interprets the frame delays of fast GIFs the same way modern browsers do

`▶ Live demo in the app` · `SPM` · `CocoaPods` · [preview GIF](motion-book/FLAnimatedImage.gif) · `.package(url: "https://github.com/Flipboard/FLAnimatedImage", from: "1.0.17")`

#### [ViewAnimator](https://github.com/marcosgriselli/ViewAnimator)
Marcos Griselli · ★ 7.3K · ⟳ 2024-03 · MIT · tag `3.1.0`

Animate collection and table view content with concise, reusable item animations.

`▶ Live demo in the app` · `SPM` · [preview GIF](motion-book/ViewAnimator.gif) · `.package(url: "https://github.com/marcosgriselli/ViewAnimator", from: "3.1.0")`

#### [Macaw](https://github.com/exyte/Macaw)
exyte · ★ 6.0K · ⟳ 2024-02 · MIT · tag `0.9.10`

Powerful and easy-to-use vector graphics Swift library with SVG support

`▶ Live demo in the app` · `SPM` · `CocoaPods` · `Carthage` · [preview GIF](motion-book/Macaw.gif) · `.package(url: "https://github.com/exyte/Macaw", from: "0.9.10")`

#### [ScrollableGraphView](https://github.com/philackm/ScrollableGraphView)
philackm · ★ 5.3K · ⟳ 2020-12 · MIT · tag `4.0.6`

An adaptive scrollable graph view for iOS to visualise simple discrete datasets. Written in Swift.

`CocoaPods` · `Carthage` · `Inactive since 2020` · [preview GIF](motion-book/ScrollableGraphView.gif)

#### [Advance](https://github.com/timdonnelly/Advance)
Storehouse · ★ 4.5K · ⟳ 2022-05 · BSD-2-Clause · tag `3.1.0`

A physics-based animation framework for direct manipulation, gestures, and playful interface motion.

`SPM` · `Archived` · `.package(url: "https://github.com/timdonnelly/Advance", from: "3.1.0")`

#### [Pow](https://github.com/EmergeTools/Pow)
EmergeTools · ★ 4.4K · ⟳ 2026-04 · MIT · tag `1.0.5`

Delightful SwiftUI effects for your app

`▶ Live demo in the app` · `SwiftUI` · `SPM` · [preview GIF](motion-book/Pow.gif) · `.package(url: "https://github.com/EmergeTools/Pow", from: "1.0.5")`

#### [Pastel](https://github.com/cruisediary/Pastel)
cruisediary · ★ 3.5K · ⟳ 2026-03 · MIT · tag `1.0.0`

🎨Gradient animation effect like Instagram

`▶ Live demo in the app` · `SPM` · `CocoaPods` · `Carthage` · [preview GIF](motion-book/Pastel.gif) · `.package(url: "https://github.com/cruisediary/Pastel", from: "1.0.0")`

#### [Stellar](https://github.com/AugustRush/Stellar)
AugustRush · ★ 2.9K · ⟳ 2019-07 · MIT · tag `0.67`

A fantastic Physical animation library for swift(Not Just Spring !!!), it is base on UIDynamic and extension to it, friendly APIs make you use it or custom your own animation very easily!

`SPM` · `CocoaPods` · `Carthage` · `Inactive since 2019` · [preview GIF](motion-book/Stellar.gif) · `.package(url: "https://github.com/AugustRush/Stellar", from: "0.67")`

#### [paper-switch](https://github.com/Ramotion/paper-switch)
Ramotion · ★ 2.9K · ⟳ 2022-01 · MIT · tag `3.1.0`

RAMPaperSwitch is a Swift material design UI module which paints over the parent view when the switch is turned on.

`SPM` · `CocoaPods` · `Carthage` · [preview GIF](motion-book/paper-switch.gif) · `.package(url: "https://github.com/Ramotion/paper-switch", from: "3.1.0")`

#### [ConfettiSwiftUI](https://github.com/simibac/ConfettiSwiftUI)
simibac · ★ 2.5K · ⟳ 2026-01 · MIT · tag `3.0.0`

SwiftUI Package for Configurable Confetti Animation 🎉

`▶ Live demo in the app` · `SwiftUI` · `SPM` · [preview GIF](motion-book/ConfettiSwiftUI.gif) · `.package(url: "https://github.com/simibac/ConfettiSwiftUI", from: "3.0.0")`

#### [Wave](https://github.com/jtrivedi/Wave)
jtrivedi · ★ 2.4K · ⟳ 2026-03 · MIT · tag `0.3.3`

Wave is a spring-based animation engine for iOS and macOS that makes it easy to create fluid, interruptible animations that feel great.

`▶ Live demo in the app` · `SPM` · [preview GIF](motion-book/Wave.gif) · `.package(url: "https://github.com/jtrivedi/Wave", from: "0.3.3")`

#### [RQShineLabel](https://github.com/zipme/RQShineLabel)
zipme · ★ 1.9K · ⟳ 2023-12 · MIT · tag `1.0.0`

A UILabel subclass that lets you animate text similar to Secret app.

`▶ Live demo in the app` · `SPM` · `CocoaPods` · [preview GIF](motion-book/RQShineLabel.gif) · `.package(url: "https://github.com/zipme/RQShineLabel", from: "1.0.0")`

#### [YLGIFImage](https://github.com/liyong03/YLGIFImage)
liyong03 · ★ 1.8K · ⟳ 2020-12 · MIT · tag `0.11`

Asynchronized GIF image class and Image viewer supporting play/stop GIF images. It just use very less memory. Following GIF usually will cost almost 600MB memory if it is fully decoded (800x600x389x4 Bytes), but using YLGIFImage, it just use about 30MB memory.

`CocoaPods` · `Inactive since 2020` · [preview GIF](motion-book/YLGIFImage.gif)

#### [AnimatedMaskLabel](https://github.com/jogendra/LoadingShimmer)
imjog · ★ 1.6K · ⟳ 2022-10 · MIT · tag `1.0.3`

Nice gradient animated label that enable an easy way to add a shimmering effect

`CocoaPods` · `Carthage` · [preview GIF](motion-book/AnimatedMaskLabel.gif)

#### [Vortex](https://github.com/twostraws/Vortex)
twostraws · ★ 1.6K · ⟳ 2026-04 · MIT · tag `1.0.4`

High-performance particle effects for SwiftUI.

`▶ Live demo in the app` · `SwiftUI` · `SPM` · [preview GIF](motion-book/Vortex.gif) · `.package(url: "https://github.com/twostraws/Vortex", from: "1.0.4")`

#### [Motion (b3ll)](https://github.com/b3ll/Motion)
b3ll · ★ 1.5K · ⟳ 2024-10 · BSD-2-Clause · tag `v0.1.5`

Animation engine for gesturally-driven user interfaces, animations, and interactions on iOS, macOS, and tvOS.

`▶ Live demo in the app` · `SPM` · [preview GIF](motion-book/Motion-b3ll.gif) · `.package(url: "https://github.com/b3ll/Motion", from: "0.1.5")`

#### [Ease](https://github.com/roberthein/Ease)
roberthein · ★ 1.3K · ⟳ 2020-07 · MIT · tag `3.2.0`

Ease is a event driven animation system that combines the observer pattern with custom spring animations as observers.

`SPM` · `CocoaPods` · `Inactive since 2020` · [preview GIF](motion-book/Ease.gif) · `.package(url: "https://github.com/roberthein/Ease", from: "3.2.0")`

#### [RevealingSplashView](https://github.com/PiXeL16/RevealingSplashView)
PiXeL16 · ★ 1.2K · ⟳ 2025-03 · MIT · tag `0.9.1`

A Splash view that animates and reveals its content, inspired by Twitter splash

`▶ Live demo in the app` · `SPM` · `CocoaPods` · `Carthage` · [preview GIF](motion-book/RevealingSplashView.gif) · `.package(url: "https://github.com/PiXeL16/RevealingSplashView", from: "0.9.1")`

#### [GlitchLabel](https://github.com/kciter/GlitchLabel)
kciter · ★ 1.0K · ⟳ 2022-12 · MIT · tag `2.1.0`

G..lit...c...hing UILa..bel fo..r iO...S

`SPM` · `CocoaPods` · `Carthage` · [preview GIF](motion-book/GlitchLabel.gif) · `.package(url: "https://github.com/kciter/GlitchLabel", from: "2.1.0")`

#### [Windless](https://github.com/ParkGwangBeom/Windless)
Interactive-Studio · ★ 947 · ⟳ 2022-07 · MIT · tag `0.1.5`

Windless makes it easy to implement invisible layout loading view.

`SPM` · `CocoaPods` · `Carthage` · [preview GIF](motion-book/Windless.gif) · `.package(url: "https://github.com/ParkGwangBeom/Windless", from: "0.1.5")`

#### [Highlighter](https://github.com/younatics/Highlighter)
younatics · ★ 921 · ⟳ 2026-10 · MIT · tag `2.1.0`

🖍Highlight whatever you want! Highlighter will magically find UI objects such as UILabel, UITextView, UITexTfield, UIButton in your UITableViewCell or other Class.

`▶ Live demo in the app` · `SPM` · `CocoaPods` · `Carthage` · [preview GIF](motion-book/Highlighter.gif) · `.package(url: "https://github.com/younatics/Highlighter", from: "2.1.0")`

#### [Liquid](https://github.com/maustinstar/liquid)
maustinstar · ★ 856 · ⟳ 2024-08 · MIT · tag `v0.0.2`

Create a playful backsplash in SwiftUI.

`▶ Live demo in the app` · `SwiftUI` · `SPM` · [preview GIF](motion-book/Liquid.gif) · `.package(url: "https://github.com/maustinstar/liquid", from: "0.0.2")`

#### [rive-ios](https://github.com/rive-app/rive-ios)
rive-app · ★ 851 · ⟳ 2026-10 · MIT · tag `6.28.1`

iOS runtime for Rive

`▶ Live demo in the app` · `SPM` · [preview GIF](motion-book/rive-ios.gif) · `.package(url: "https://github.com/rive-app/rive-ios", from: "6.28.1")`

#### [URWeatherView](https://github.com/Urtaq/URWeatherView)
jegumhon · ★ 447 · ⟳ 2019-01 · MIT · tag `0.7.0`

Show the weather effects onto view written in Swift3

`CocoaPods` · `Carthage` · `Inactive since 2019` · [preview GIF](motion-book/URWeatherView.gif)

#### [AnimateText](https://github.com/jasudev/AnimateText)
jasudev · ★ 432 · ⟳ 2024-02 · MIT · tag `0.5.0`

This library for animating text. Developed with SwiftUI. This library supports iOS/macOS.

`▶ Live demo in the app` · `SwiftUI` · `SPM` · [preview GIF](motion-book/AnimateText.gif) · `.package(url: "https://github.com/jasudev/AnimateText", from: "0.5.0")`

#### [Gecco](https://github.com/xai3/Gecco)
yukiasai · ★ 19 · ⟳ 2020-09 · MIT · tag `2.0.0`

Simply highlight items for your tutorial walkthrough, written in Swift. Gecco means Moonlight in Japanese.

`CocoaPods` · `Carthage` · `Inactive since 2020` · [preview GIF](motion-book/Gecco.gif)

### Transition

#### [Hero](https://github.com/HeroTransitions/Hero)
lkzhao · ★ 22K · ⟳ 2025-01 · MIT · tag `1.6.4`

Hero is a library for building iOS view controller transitions. It provides a layer on top of the UIKit's cumbersome transition APIs. Making custom transitions an easy task for developers.

`▶ Live demo in the app` · `SPM` · `CocoaPods` · `Carthage` · [preview GIF](motion-book/Hero.gif) · `.package(url: "https://github.com/HeroTransitions/Hero", from: "1.6.4")`

#### [XLPagerTabStrip](https://github.com/xmartlabs/XLPagerTabStrip)
xmartlabs · ★ 7.0K · ⟳ 2023-11 · MIT · tag `9.1.0`

XLPagerTabStrip is a Container View Controller that allows us to switch easily among a collection of view controllers. Pan gesture can be used to move on to next or previous view controller. It shows a interactive indicator of the current, previous, next child view controllers.

`▶ Live demo in the app` · `SPM` · `CocoaPods` · `Carthage` · [preview GIF](motion-book/XLPagerTabStrip.gif) · `.package(url: "https://github.com/xmartlabs/XLPagerTabStrip", from: "9.1.0")`

#### [AnimatedCollectionViewLayout](https://github.com/KelvinJin/AnimatedCollectionViewLayout)
KelvinJin · ★ 4.9K · ⟳ 2020-09 · MIT · tag `1.1.0`

Animated UIButton of Loading Animation and Transition Animation.

`▶ Live demo in the app` · `SPM` · `CocoaPods` · `Inactive since 2020` · [preview GIF](motion-book/AnimatedCollectionViewLayout.gif) · `.package(url: "https://github.com/KelvinJin/AnimatedCollectionViewLayout", from: "1.1.0")`

#### [Gemini](https://github.com/shoheiyokoyama/Gemini)
shoheiyokoyama · ★ 3.3K · ⟳ 2025-06 · MIT · tag `1.4.0`

Gemini is rich scroll based animation framework for iOS, written in Swift.

`CocoaPods` · `Carthage` · [preview GIF](motion-book/Gemini.gif)

#### [BubbleTransition](https://github.com/andreamazz/BubbleTransition)
andreamazz · ★ 3.3K · ⟳ 2020-11 · MIT · tag `3.1.1`

A custom modal transition that presents and dismiss a controller inside an expanding and shrinking bubble.

`SPM` · `CocoaPods` · `Carthage` · `Inactive since 2020` · [preview GIF](motion-book/BubbleTransition.gif) · `.package(url: "https://github.com/andreamazz/BubbleTransition", from: "3.1.1")`

#### [BWWalkthrough](https://github.com/ariok/BWWalkthrough)
ariok · ★ 2.7K · ⟳ 2021-02 · MIT · tag `4.0.2`

BWWalkthrough (BWWT) is a class that helps you create Walkthroughs for your iOS Apps. It differs from other similar classes in that there is no rigid template; BWWT is just a layer placed over your controllers that gives you complete freedom on the design of your views.

`SPM` · `CocoaPods` · `Carthage` · [preview GIF](motion-book/BWWalkthrough.gif) · `.package(url: "https://github.com/ariok/BWWalkthrough", from: "4.0.2")`

#### [AnimatedTransitionGallery](https://github.com/shu223/AnimatedTransitionGallery)
shu223 · ★ 2.5K · ⟳ 2024-04

Collection of custom animated transitions for iOS using UIViewControllerAnimatedTransitioning protocol.

[preview GIF](motion-book/AnimatedTransitionGallery.gif)

#### [AMWaveTransition](https://github.com/andreamazz/AMWaveTransition)
andreamazz · ★ 2.3K · ⟳ 2020-06 · MIT · tag `0.6.2`

Custom transition between viewcontrollers holding tableviews. Each cell is animated to simulate a 'wave effect'.

`CocoaPods` · `Carthage` · `Inactive since 2020` · [preview GIF](motion-book/AMWaveTransition.gif)

#### [TKSubmitTransition](https://github.com/takuoka/TKSubmitTransition)
entotsu · ★ 2.3K · ⟳ 2019-12 · MIT · tag `3.1.1`

Animated UIButton of Loading Animation and Transition Animation.

`CocoaPods` · `Inactive since 2019` · [preview GIF](motion-book/TKSubmitTransition.gif)

#### [ElasticTransition](https://github.com/lkzhao/ElasticTransition)
lkzhao · ★ 2.2K · ⟳ 2020-05 · MIT · tag `3.1.1`

A UIKit custom transition that simulates an elastic drag. Written in Swift.

`CocoaPods` · `Inactive since 2020` · [preview GIF](motion-book/ElasticTransition.gif)

#### [preview-transition](https://github.com/Ramotion/preview-transition)
Ramotion · ★ 2.1K · ⟳ 2020-04 · MIT · tag `4.1.0`

PreviewTransition is a simple preview gallery controller

`▶ Live demo in the app` · `SPM` · `CocoaPods` · `Carthage` · `Inactive since 2020` · [preview GIF](motion-book/preview-transition.gif) · `.package(url: "https://github.com/Ramotion/preview-transition", from: "4.1.0")`

#### [PinterestSwift](https://github.com/demonnico/PinterestSwift)
demonnico · ★ 1.9K · ⟳ 2020-06 · MIT

This is a Swift based demo project to show how to make the transition Pinterest liked.

`Inactive since 2020` · [preview GIF](motion-book/PinterestSwift.gif)

#### [CKWaveCollectionViewTransition](https://github.com/CezaryKopacz/CKWaveCollectionViewTransition)
CezaryKopacz · ★ 1.8K · ⟳ 2019-10 · MIT · tag `v1.2`

Cool wave like transition between two or more UICollectionView

`CocoaPods` · `Inactive since 2019` · [preview GIF](motion-book/CKWaveCollectionViewTransition.gif)

#### [Motion](https://github.com/CosmicMind/Motion)
CosmicMind · ★ 1.8K · ⟳ 2020-01 · MIT · tag `3.1.3`

A Material-inspired motion engine for transitions, transforms, and interactive presentation work.

`SPM` · `Inactive since 2020` · `.package(url: "https://github.com/CosmicMind/Motion", from: "3.1.3")`

#### [Transmission](https://github.com/nathantannar4/Transmission)
nathantannar4 · ★ 1.2K · ⟳ 2026-10 · BSD-2-Clause · tag `3.0.0`

Bridges UIKit presentation APIs to a SwiftUI API so you can use presentation controllers, interactive transitions and more.

`▶ Live demo in the app` · `SwiftUI` · `SPM` · [preview GIF](motion-book/Transmission.gif) · `.package(url: "https://github.com/nathantannar4/Transmission", from: "3.0.0")`

#### [JTMaterialTransition](https://github.com/johnvuko/JTMaterialTransition)
jonathantribouharet · ★ 949 · ⟳ 2019-01 · MIT · tag `2.0.3`

An iOS transition for controllers based on material design.

`▶ Live demo in the app` · `SPM` · `CocoaPods` · `Inactive since 2019` · [preview GIF](motion-book/JTMaterialTransition.gif) · `.package(url: "https://github.com/johnvuko/JTMaterialTransition", from: "2.0.3")`

### UI

#### [IBAnimatable](https://github.com/IBAnimatable/IBAnimatable)
IBAnimatable · ★ 8.6K · ⟳ 2023-02 · MIT · tag `6.1.0`

Design and prototype customized UI, interaction, navigation, transition and animation for App Store ready Apps in Interface Builder with IBAnimatable.

`▶ Live demo in the app` · `SPM` · `CocoaPods` · `Carthage` · [preview GIF](motion-book/IBAnimatable.gif) · `.package(url: "https://github.com/IBAnimatable/IBAnimatable", from: "6.1.0")`

#### [LTMorphingLabel](https://github.com/lexrus/LTMorphingLabel)
lexrus · ★ 8.1K · ⟳ 2026-03 · MIT · tag `0.9.3`

A morphing UILabel subclass written in Swift. The .Scale effect mimicked Apple's QuickType animation of iOS 8 in WWDC 2014. New morphing effects are available as Swift extensions.

`▶ Live demo in the app` · `SPM` · `CocoaPods` · `Carthage` · [preview GIF](motion-book/LTMorphingLabel.gif) · `.package(url: "https://github.com/lexrus/LTMorphingLabel", from: "0.9.3")`

#### [Cards](https://github.com/PaoloCuscela/Cards)
PaoloCuscela · ★ 4.2K · ⟳ 2023-04 · MIT · tag `1.4.0`

Awesome iOS 11 appstore cards in swift 4.

`CocoaPods` · [preview GIF](motion-book/Cards.gif)

#### [StarWars.iOS](https://github.com/Yalantis/StarWars.iOS)
Yalantis · ★ 3.8K · ⟳ 2022-10 · MIT · tag `4.0`

This component implements transition animation to crumble view-controller into tiny pieces.

`CocoaPods` · [preview GIF](motion-book/StarWars.iOS.gif)

#### [DKNightVersion](https://github.com/draveness/DKNightVersion)
Draveness · ★ 3.5K · ⟳ 2019-09 · MIT · tag `2.4.3`

Manage Colors, Integrate Night/Multiple Themes

`CocoaPods` · `Carthage` · `Archived` · [preview GIF](motion-book/DKNightVersion.gif)

#### [RazzleDazzle](https://github.com/IFTTT/RazzleDazzle)
IFTTT · ★ 3.3K · ⟳ 2023-10 · MIT · tag `0.1.5`

Create scroll-driven onboarding and storytelling animations without hand-wiring every offset.

`CocoaPods`

#### [Presentation](https://github.com/hyperoslo/Presentation)
hyperoslo · ★ 3.1K · ⟳ 2020-06 · MIT · tag `4.1.2`

Looking for the easiest way of presenting something in your iOS app? Then you are in the right place. Presentation will help you make your tutorials, release notes and any kind of animated pages with the minimum amount of effort.

`CocoaPods` · `Carthage` · `Inactive since 2020` · [preview GIF](motion-book/Presentation.gif)

#### [Inferno](https://github.com/twostraws/Inferno)
twostraws · ★ 2.9K · ⟳ 2026-05 · MIT · tag `1.1.0`

Metal shaders for SwiftUI.

`▶ Live demo in the app` · `SwiftUI` · `SPM` · [preview GIF](motion-book/Inferno.gif) · `.package(url: "https://github.com/twostraws/Inferno", from: "1.1.0")`

#### [Segmentio](https://github.com/Yalantis/Segmentio)
Yalantis · ★ 2.5K · ⟳ 2024-08 · MIT · tag `3.0`

Animated top/bottom segmented control written in Swift.

`▶ Live demo in the app` · `SPM` · `CocoaPods` · `Carthage` · [preview GIF](motion-book/Segmentio.gif) · `.package(url: "https://github.com/Yalantis/Segmentio", from: "3.0")`

#### [MarkdownView](https://github.com/keitaoouchi/MarkdownView)
keitaoouchi · ★ 2.2K · ⟳ 2026-10 · MIT · tag `2.1.1`

MarkdownView is a WKWebView based UI element, and internally use bootstrap, highlight.js, markdown-it.

`▶ Live demo in the app` · `SPM` · `CocoaPods` · `Carthage` · [preview GIF](motion-book/MarkdownView.gif) · `.package(url: "https://github.com/keitaoouchi/MarkdownView", from: "2.1.1")`

#### [Glur](https://github.com/joogps/Glur)
joogps · ★ 2.1K · ⟳ 2026-10 · MIT · tag `2.1`

A library for progressive blurs in SwiftUI.

`▶ Live demo in the app` · `SwiftUI` · `SPM` · [preview GIF](motion-book/Glur.gif) · `.package(url: "https://github.com/joogps/Glur", from: "2.1")`

#### [fluid-slider](https://github.com/Ramotion/fluid-slider)
Ramotion · ★ 2.0K · ⟳ 2022-06 · MIT · tag `1.1.0`

A slider widget with a popup bubble displaying the precise value selected.

`SPM` · `CocoaPods` · `Carthage` · [preview GIF](motion-book/fluid-slider.gif) · `.package(url: "https://github.com/Ramotion/fluid-slider", from: "1.1.0")`

#### [SwiftUI-Shimmer](https://github.com/markiv/SwiftUI-Shimmer)
markiv · ★ 1.7K · ⟳ 2024-08 · MIT · tag `1.5.1`

Shimmer is a super-light modifier that adds a shimmering effect to any SwiftUI View, for example, to show that an operation is in progress. It works well on light and dark modes, and across iOS, macOS, tvOS, watchOS and visionOS.

`▶ Live demo in the app` · `SwiftUI` · `SPM` · [preview GIF](motion-book/SwiftUI-Shimmer.gif) · `.package(url: "https://github.com/markiv/SwiftUI-Shimmer", from: "1.5.1")`

#### [ScalingHeaderScrollView](https://github.com/exyte/ScalingHeaderScrollView)
exyte · ★ 1.5K · ⟳ 2026-10 · MIT · tag `3.1.0`

A scroll view with a sticky header which shrinks as you scroll. Written with SwiftUI.

`▶ Live demo in the app` · `SwiftUI` · `SPM` · [preview GIF](motion-book/ScalingHeaderScrollView.gif) · `.package(url: "https://github.com/exyte/ScalingHeaderScrollView", from: "3.1.0")`

#### [YNSearch](https://github.com/younatics/YNSearch)
younatics · ★ 1.2K · ⟳ 2026-10 · MIT · tag `3.1.0`

✨Awesome search view, written in Swift 3, appears search view like Pinterest Search view. You can fully customize this library. You can also use this library with Realm!

`▶ Live demo in the app` · `SPM` · `CocoaPods` · `Carthage` · [preview GIF](motion-book/YNSearch.gif) · `.package(url: "https://github.com/younatics/YNSearch", from: "3.1.0")`

#### [Shiny](https://github.com/maustinstar/shiny)
maustinstar · ★ 1.1K · ⟳ 2024-07 · MIT · tag `v0.0.1`

Shiny uses your gyroscope to simulate lighting and motion effects on colors. Works on almost every SwiftUI View.

`▶ Live demo in the app` · `SwiftUI` · `SPM` · [preview GIF](motion-book/Shiny.gif) · `.package(url: "https://github.com/maustinstar/shiny", from: "0.0.1")`

#### [AIFlatSwitch](https://github.com/cocoatoucher/AIFlatSwitch)
cocoatoucher · ★ 963 · ⟳ 2022-06 · MIT · tag `1.0.8`

A smooth, nice looking and IBDesignable flat design switch for iOS. Can be used instead of UISwitch. Inspired by Creativedash's Dribbble post

`SPM` · `CocoaPods` · [preview GIF](motion-book/AIFlatSwitch.gif) · `.package(url: "https://github.com/cocoatoucher/AIFlatSwitch", from: "1.0.8")`

#### [MediaBrowser](https://github.com/younatics/MediaBrowser)
younatics · ★ 646 · ⟳ 2026-10 · MIT · tag `3.1.0`

🏞 MediaBrowser can display one or more images or videos by providing either UIImage objects, PHAsset objects, or URLs to library assets, web images/videos or local files. MediaBrowser handles the downloading and caching of photos from the web seamlessly. Photos can be zoomed and panned, and optional (customisable) captions can be displayed. This can also be used to allow the user to select one or more photos using either the grid or main image view.

`▶ Live demo in the app` · `SPM` · `CocoaPods` · `Carthage` · [preview GIF](motion-book/MediaBrowser.gif) · `.package(url: "https://github.com/younatics/MediaBrowser", from: "3.1.0")`

#### [FluidGradient](https://github.com/Cindori/FluidGradient)
Cindori · ★ 439 · ⟳ 2024-03 · MIT · tag `1.0.0`

A fluid, animated gradient implemented with CoreAnimation and SwiftUI.

`▶ Live demo in the app` · `SwiftUI` · `SPM` · [preview GIF](motion-book/FluidGradient.gif) · `.package(url: "https://github.com/Cindori/FluidGradient", from: "1.0.0")`

#### [PARTagPicker](https://github.com/paulrolfe/PARTagPicker)
paulrolfe · ★ 365 · ⟳ 2019-06 · MIT · tag `1.4.0`

This pod provides a view controller for choosing and creating tags in the style of wordpress or tumblr. This tag picker was originally used in the Intrepid Pursuits app, Slate.

`CocoaPods` · `Inactive since 2019` · [preview GIF](motion-book/PARTagPicker.gif)

### Menu

#### [animated-tab-bar](https://github.com/Ramotion/animated-tab-bar)
Ramotion · ★ 11K · ⟳ 2022-01 · MIT · tag `5.1.0`

RAMAnimatedTabBarController is a Swift module for adding animation to tabbar items.

`▶ Live demo in the app` · `SPM` · `CocoaPods` · `Carthage` · [preview GIF](motion-book/animated-tab-bar.gif) · `.package(url: "https://github.com/Ramotion/animated-tab-bar", from: "5.1.0")`

#### [SideMenu](https://github.com/jonkykong/SideMenu)
jonkykong · ★ 5.8K · ⟳ 2023-02 · MIT · tag `6.5.0`

Simple side menu control for iOS in Swift inspired by Facebook. Right and Left sides. No coding required. iOS 8+.

`▶ Live demo in the app` · `SPM` · `CocoaPods` · `Carthage` · [preview GIF](motion-book/SideMenu.gif) · `.package(url: "https://github.com/jonkykong/SideMenu", from: "6.5.0")`

#### [circle-menu](https://github.com/Ramotion/circle-menu)
Ramotion · ★ 3.4K · ⟳ 2022-07 · MIT · tag `4.1.0`

This project is maintained by Ramotion, Inc. We specialize in the designing and coding of custom UI for Mobile Apps and Websites.

`▶ Live demo in the app` · `SPM` · `CocoaPods` · `Carthage` · [preview GIF](motion-book/circle-menu.gif) · `.package(url: "https://github.com/Ramotion/circle-menu", from: "4.1.0")`

#### [SlideMenuControllerSwift](https://github.com/dekatotoro/SlideMenuControllerSwift)
dekatotoro · ★ 3.4K · ⟳ 2023-09 · MIT · tag `2.2.0`

iOS Slide Menu View based on Google+, iQON, Feedly, Ameba iOS app. It is written in pure swift.

`CocoaPods` · `Carthage` · [preview GIF](motion-book/SlideMenuControllerSwift.gif)

#### [GuillotineMenu](https://github.com/Yalantis/GuillotineMenu)
Yalantis · ★ 2.9K · ⟳ 2020-04 · MIT · tag `3.0.2`

Our Guillotine Menu Transitioning Animation implemented in Swift reminds a bit of a notorious killing machine.

`CocoaPods` · `Inactive since 2020` · [preview GIF](motion-book/GuillotineMenu.gif)

#### [Side-Menu.iOS](https://github.com/Yalantis/Side-Menu.iOS)
Yalantis · ★ 2.7K · ⟳ 2020-04 · MIT · tag `2.0.2`

Animated side menu with customizable UI. Made in Yalantis.

`CocoaPods` · `Inactive since 2020` · [preview GIF](motion-book/Side-Menu.iOS.gif)

#### [YNDropDownMenu](https://github.com/younatics/YNDropDownMenu)
younatics · ★ 1.3K · ⟳ 2026-10 · MIT · tag `4.1.0`

✨The eligible dropdown menu, written in Swift 3, appears dropdown menu to display a view of related items when a user click on the dropdown menu. You can customize dropdown view whatever you like (e.g. UITableView, UICollectionView... etc)

`▶ Live demo in the app` · `SPM` · `CocoaPods` · `Carthage` · [preview GIF](motion-book/YNDropDownMenu.gif) · `.package(url: "https://github.com/younatics/YNDropDownMenu", from: "4.1.0")`

#### [AnimatedTabBar (exyte)](https://github.com/exyte/AnimatedTabBar)
exyte · ★ 557 · ⟳ 2026-07 · MIT · tag `1.0.1`

A tabbar with a number of preset animations written in pure SwiftUI

`SwiftUI` · `SPM` · `.package(url: "https://github.com/exyte/AnimatedTabBar", from: "1.0.1")`

### Alert

#### [NotificationBanner](https://github.com/Daltron/NotificationBanner)
Daltron · ★ 4.9K · ⟳ 2024-07 · MIT · tag `3.2.0`

NotificationBanner is an extremely customizable and lightweight library that makes the task of displaying in app notification banners and drop down alerts an absolute breeze in iOS.

`▶ Live demo in the app` · `SPM` · `CocoaPods` · `Carthage` · [preview GIF](motion-book/NotificationBanner.gif) · `.package(url: "https://github.com/Daltron/NotificationBanner", from: "3.2.0")`

#### [CRToast](https://github.com/cruffenach/CRToast)
cruffenach · ★ 4.1K · ⟳ 2024-05 · MIT · tag `0.0.9`

CRToast is a library that allows you to easily create notifications that appear on top of or by pushing out the status bar or navigation bar.

`▶ Live demo in the app` · `CocoaPods` · `Carthage` · [preview GIF](motion-book/CRToast.gif)

#### [PopupView](https://github.com/exyte/PopupView)
exyte · ★ 4.1K · ⟳ 2026-10 · MIT · tag `5.0.8`

Toasts and popups library written with SwiftUI

`▶ Live demo in the app` · `SwiftUI` · `SPM` · [preview GIF](motion-book/PopupView.gif) · `.package(url: "https://github.com/exyte/PopupView", from: "5.0.8")`

#### [PopupDialog](https://github.com/Orderella/PopupDialog)
Orderella · ★ 4.0K · ⟳ 2024-02 · MIT · tag `1.1.1`

A simple, customizable popup dialog for iOS written in Swift. Replaces UIAlertController alert style.

`▶ Live demo in the app` · `SPM` · `CocoaPods` · `Carthage` · [preview GIF](motion-book/PopupDialog.gif) · `.package(url: "https://github.com/Orderella/PopupDialog", from: "1.1.1")`

#### [Popovers](https://github.com/aheze/Popovers)
aheze · ★ 2.2K · ⟳ 2025-02 · MIT · tag `1.3.2`

A library to present popovers. Simple, modern, and highly customizable. Not boring!

`▶ Live demo in the app` · `SwiftUI` · `SPM` · [preview GIF](motion-book/Popovers.gif) · `.package(url: "https://github.com/aheze/Popovers", from: "1.3.2")`

#### [SweetAlert-iOS](https://github.com/codestergit/SweetAlert-iOS)
codestergit · ★ 2.0K · ⟳ 2020-03 · MIT · tag `v0.9`

Beautiful Animated custom Alert View inspired from javascript library SweetAlert. Written in Swift this SweetAlertView can be used in Swift and Objective-C projects. SweetAlertView provides live intutive experience to user actions.It can be used in place of UIAlertView and UIAlertController

`▶ Live demo in the app` · `Inactive since 2020` · [preview GIF](motion-book/SweetAlert-iOS.gif)

#### [SDCAlertView](https://github.com/sberrevoets/SDCAlertView)
sberrevoets · ★ 1.8K · ⟳ 2025-01 · MIT · tag `12.0.5`

SDCAlertView started out as an alert that looked identical to UIAlertView, but had support for a custom content view. With the introduction of UIAlertController in iOS 8, the project was updated to the more modern API that UIAlertController brought.

`▶ Live demo in the app` · `SPM` · `CocoaPods` · `Carthage` · [preview GIF](motion-book/SDCAlertView.gif) · `.package(url: "https://github.com/sberrevoets/SDCAlertView", from: "12.0.5")`

#### [CDAlertView](https://github.com/candostdagdeviren/CDAlertView)
candostdagdeviren · ★ 1.1K · ⟳ 2026-08 · MIT · tag `0.11.0`

CDAlertView is highly customizable alert popup written in Swift 3. Usage is similar to UIAlertController.

`CocoaPods` · `Carthage` · [preview GIF](motion-book/CDAlertView.gif)

#### [MIBlurPopup](https://github.com/MarioIannotta/MIBlurPopup)
MarioIannotta · ★ 598 · ⟳ 2020-03 · MIT · tag `1.0.0`

MIBlurPopup lets you create amazing popups with a blurred background

`▶ Live demo in the app` · `CocoaPods` · `Inactive since 2020` · [preview GIF](motion-book/MIBlurPopup.gif)

#### [TKSwarmAlert](https://github.com/takuoka/TKSwarmAlert)
entotsu · ★ 573 · ⟳ 2019-03 · MIT · tag `0.1.3`

Animated alert library like Swarm app.

`CocoaPods` · `Carthage` · `Inactive since 2019` · [preview GIF](motion-book/TKSwarmAlert.gif)

#### [GoogleWearAlert](https://github.com/ashrobo/GoogleWearAlert)
AshRobinson · ★ 417 · ⟳ 2016-10 · MIT

An Android Wear style confirmation view for iOS

`Inactive since 2016` · [preview GIF](motion-book/GoogleWearAlert.gif)

### Collection View

#### [expanding-collection](https://github.com/Ramotion/expanding-collection)
Ramotion · ★ 5.5K · ⟳ 2020-04 · MIT · tag `3.1.0`

This project aims to provide a simple and customizable pull to refresh implementation.

`▶ Live demo in the app` · `SPM` · `CocoaPods` · `Carthage` · `Inactive since 2020` · [preview GIF](motion-book/expanding-collection.gif) · `.package(url: "https://github.com/Ramotion/expanding-collection", from: "3.1.0")`

#### [Koloda](https://github.com/Yalantis/Koloda)
Yalantis · ★ 5.4K · ⟳ 2024-05 · MIT · tag `4.3.1`

KolodaView is a class designed to simplify the implementation of Tinder like cards on iOS.

`▶ Live demo in the app` · `CocoaPods` · `Carthage` · [preview GIF](motion-book/Koloda.gif)

#### [CSStickyHeaderFlowLayout](https://github.com/CSStickyHeaderFlowLayout/CSStickyHeaderFlowLayout)
CSStickyHeaderFlowLayout · ★ 5.0K · ⟳ 2021-07 · MIT · tag `0.2.12`

UICollectionView replacement of UITableView. Do even more like Parallax Header, Sticky Section Header. Made for iOS 7.

`CocoaPods` · `Carthage` · [preview GIF](motion-book/CSStickyHeaderFlowLayout.gif)

#### [Grid (exyte)](https://github.com/exyte/Grid)
exyte · ★ 2.1K · ⟳ 2026-09 · MIT · tag `1.5.0`

The most powerful Grid container missed in SwiftUI

`▶ Live demo in the app` · `SwiftUI` · `SPM` · [preview GIF](motion-book/Grid-exyte.gif) · `.package(url: "https://github.com/exyte/Grid", from: "1.5.0")`

#### [GSKStretchyHeaderView](https://github.com/gskbyte/GSKStretchyHeaderView)
gskbyte · ★ 1.7K · ⟳ 2024-08 · MIT · tag `1.0.4`

GSKStretchyHeaderView is an implementation of the stretchy header paradigm as seen on many apps, like Twitter, Spotify or airbnb.

`CocoaPods` · `Carthage` · [preview GIF](motion-book/GSKStretchyHeaderView.gif)

#### [SwiftSpreadsheet](https://github.com/stuffrabbit/SwiftSpreadsheet)
stuffrabbit · ★ 637 · ⟳ 2019-10 · MIT · tag `1.2.1`

Spreadsheet CollectionViewLayout in Swift. Fully customizable.

`SPM` · `CocoaPods` · `Inactive since 2019` · [preview GIF](motion-book/SwiftSpreadsheet.gif) · `.package(url: "https://github.com/stuffrabbit/SwiftSpreadsheet", from: "1.2.1")`

#### [MMCardView](https://github.com/MillmanY/MMCardView)
MillmanY · ★ 565 · ⟳ 2021-10 · MIT · tag `1.1.2`

Custom CollectionView like Wallet App

`CocoaPods` · [preview GIF](motion-book/MMCardView.gif)

### Table View

#### [folding-cell](https://github.com/Ramotion/folding-cell)
Ramotion · ★ 10K · ⟳ 2024-04 · MIT · tag `5.0.2`

FoldingCell is an expanding content cell inspired by folding paper material

`▶ Live demo in the app` · `SPM` · `CocoaPods` · `Carthage` · [preview GIF](motion-book/folding-cell.gif) · `.package(url: "https://github.com/Ramotion/folding-cell", from: "5.0.2")`

#### [SwipeCellKit](https://github.com/SwipeCellKit/SwipeCellKit)
jerkoch · ★ 6.3K · ⟳ 2024-05 · MIT · tag `2.7.1`

Swipeable UITableViewCell based on the stock Mail.app, implemented in Swift.

`▶ Live demo in the app` · `SPM` · `CocoaPods` · `Carthage` · [preview GIF](motion-book/SwipeCellKit.gif) · `.package(url: "https://github.com/SwipeCellKit/SwipeCellKit", from: "2.7.1")`

#### [Pull-to-Refresh.Rentals-iOS](https://github.com/Yalantis/Pull-to-Refresh.Rentals-iOS)
Yalantis · ★ 2.1K · ⟳ 2018-06 · MIT · tag `1.0`

This project aims to provide a simple and customizable pull to refresh implementation.

`▶ Live demo in the app` · `CocoaPods` · `Inactive since 2018` · [preview GIF](motion-book/Pull-to-Refresh.Rentals-iOS.gif)

#### [elongation-preview](https://github.com/Ramotion/elongation-preview)
Ramotion · ★ 888 · ⟳ 2020-04 · MIT · tag `1.1.1`

ElongationPreview is an elegant push-pop style view controller

`SPM` · `CocoaPods` · `Carthage` · `Inactive since 2020` · [preview GIF](motion-book/elongation-preview.gif) · `.package(url: "https://github.com/Ramotion/elongation-preview", from: "1.1.1")`

#### [YNExpandableCell](https://github.com/younatics/YNExpandableCell)
younatics · ★ 451 · ⟳ 2026-10 · MIT · tag `2.1.0`

✨Easiest usage of expandable & collapsible cell for iOS, written in Swift 3. You can customize expandable UITableViewCell whatever you like. YNExpandableCell is made because insertRows and deleteRows is hard to use. You can just inheirt YNTableViewDelegate and add one more method func tableView(_ tableView: YNTableView, expandCellAt indexPath) -> UITableViewCell?

`▶ Live demo in the app` · `SPM` · `CocoaPods` · `Carthage` · [preview GIF](motion-book/YNExpandableCell.gif) · `.package(url: "https://github.com/younatics/YNExpandableCell", from: "2.1.0")`

### Indicator

#### [NVActivityIndicatorView](https://github.com/ninjaprox/NVActivityIndicatorView)
ninjaprox · ★ 11K · ⟳ 2026-03 · MIT · tag `5.2.0`

NVActivityIndicatorView is a collection of awesome loading animations.

`▶ Live demo in the app` · `SPM` · `CocoaPods` · `Carthage` · [preview GIF](motion-book/NVActivityIndicatorView.gif) · `.package(url: "https://github.com/ninjaprox/NVActivityIndicatorView", from: "5.2.0")`

#### [PKHUD](https://github.com/pkluz/PKHUD)
pkluz · ★ 3.8K · ⟳ 2023-02 · MIT · tag `5.4.0`

A Swift based reimplementation of the Apple HUD (Volume, Ringer, Rotation,…) for iOS 8.

`▶ Live demo in the app` · `SPM` · `CocoaPods` · `Carthage` · [preview GIF](motion-book/PKHUD.gif) · `.package(url: "https://github.com/pkluz/PKHUD", from: "5.4.0")`

#### [ActivityIndicatorView](https://github.com/exyte/ActivityIndicatorView)
exyte · ★ 1.7K · ⟳ 2026-09 · MIT · tag `2.0.2`

A number of preset loading indicators created with SwiftUI

`▶ Live demo in the app` · `SwiftUI` · `SPM` · [preview GIF](motion-book/ActivityIndicatorView.gif) · `.package(url: "https://github.com/exyte/ActivityIndicatorView", from: "2.0.2")`

#### [TKRubberIndicator](https://github.com/tbxark/TKRubberIndicator)
TBXark · ★ 1.5K · ⟳ 2026-09 · MIT · tag `2.0.0`

A rubber animation pagecontrol

`▶ Live demo in the app` · `SPM` · `CocoaPods` · `Carthage` · [preview GIF](motion-book/TKRubberIndicator.gif) · `.package(url: "https://github.com/tbxark/TKRubberIndicator", from: "2.0.0")`

#### [BusyNavigationBar](https://github.com/gmertk/BusyNavigationBar)
gmertk · ★ 980 · ⟳ 2017-05 · MIT · tag `2.0.0`

A UINavigationBar extension to show loading effects above navigation bar's background.

`CocoaPods` · `Carthage` · `Inactive since 2017` · [preview GIF](motion-book/BusyNavigationBar.gif)

#### [SpringIndicator](https://github.com/KyoheiG3/SpringIndicator)
KyoheiG3 · ★ 271 · ⟳ 2020-09 · MIT · tag `4.0.0`

SpringIndicator is indicator and PullToRefresh. Inspired by Material design components.

`SPM` · `CocoaPods` · `Carthage` · `Inactive since 2020` · [preview GIF](motion-book/SpringIndicator.gif) · `.package(url: "https://github.com/KyoheiG3/SpringIndicator", from: "4.0.0")`

## About

MotionBook started in 2017 as the catalog behind the [MotionBook iOS app](https://apps.apple.com/app/id1205163580) (Apple featured it as a best new app). The 2026 app runs the libraries live again on the current SDK; this repository is the list the app, its users and coding agents read. GIFs under `motion-book/` are the app's preview assets. `Data/motionbook.json` is the 2017 format kept for old clients.

Made by [younatics](https://github.com/younatics). MIT.
