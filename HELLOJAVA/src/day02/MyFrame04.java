package day02;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JFormattedTextField;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyFrame04 extends JFrame {

	private JPanel contentPane;
	private JTextField tf1;
	private JTextField tf2;
	private JTextField tf3;
	private JButton btnNewButton;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyFrame04 frame = new MyFrame04();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MyFrame04() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf1 = new JTextField();
		tf1.setBounds(21, 64, 130, 26);
		contentPane.add(tf1);
		tf1.setColumns(10);
		
		JLabel lblNewLabel = new JLabel("부터");
		lblNewLabel.setBounds(163, 69, 61, 16);
		contentPane.add(lblNewLabel);
		
		tf2 = new JTextField();
		tf2.setBounds(235, 64, 130, 26);
		contentPane.add(tf2);
		tf2.setColumns(10);
		
		tf3 = new JTextField();
		tf3.setBounds(207, 136, 130, 26);
		contentPane.add(tf3);
		tf3.setColumns(10);
		
		JButton btn = new JButton("까지의 합은");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int numA = Integer.parseInt(tf1.getText());
				int numB = Integer.parseInt(tf2.getText());
				int result = 0;
				
				for(int i=numA ; i<=numB; i++) {
					result += i;
				}
				
				tf3.setText(String.valueOf(result));
			}
		});
		btn.setBounds(78, 136, 117, 29);
		contentPane.add(btn);
		
		btnNewButton = new JButton("까지의 곱은");
		btnNewButton.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int numA = Integer.parseInt(tf1.getText());
				int numB = Integer.parseInt(tf2.getText());
				int result = 1;
				
				for(int i=numA ; i<=numB; i++) {
					result *= i;
				}
				
				tf3.setText(String.valueOf(result));
			}
		});
		btnNewButton.setBounds(78, 165, 117, 29);
		contentPane.add(btnNewButton);
	}
}
