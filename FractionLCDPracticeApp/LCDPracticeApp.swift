import SwiftUI

@main
struct LCDPracticeApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}

struct ContentView: View {
    @State private var denominator1: String = ""
    @State private var denominator2: String = ""
    @State private var resultText: String = ""

    private func gcd(_ a: Int, _ b: Int) -> Int {
        var a = a
        var b = b
        while b != 0 {
            let temp = a % b
            a = b
            b = temp
        }
        return a
    }

    private func lcm(_ a: Int, _ b: Int) -> Int {
        return abs(a * b) / gcd(a, b)
    }

    var body: some View {
        NavigationView {
            Form {
                Section(header: Text("Enter Denominators")) {
                    TextField("First Denominator", text: $denominator1)
                        .keyboardType(.numberPad)
                    TextField("Second Denominator", text: $denominator2)
                        .keyboardType(.numberPad)
                }
                Button("Find LCD") {
                    if let d1 = Int(denominator1), let d2 = Int(denominator2), d1 > 0, d2 > 0 {
                        let lcd = lcm(d1, d2)
                        resultText = "Least Common Denominator: \(lcd)"
                    } else {
                        resultText = "Please enter valid positive integers."
                    }
                }
                Section {
                    Text(resultText)
                        .font(.headline)
                }
            }
            .navigationTitle("LCD Practice")
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
